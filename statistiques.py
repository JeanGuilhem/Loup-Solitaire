"""
Statistiques des parties jouées (cf. game_stats.py). Page cachée : /statistiques,
protégée par le mot de passe des secrets ([stats] password).
"""
import hmac

import pandas as pd
import streamlit as st

from game_stats import load_events
from variable import BOOKS, KAI, STARTING_ITEM_TABLE, WEAPON_MASTERY_TABLE

st.set_page_config(page_title="Statistiques", page_icon="📊", layout="wide")
st.title("📊 Statistiques des parties")


def check_password() -> bool:
    try:
        expected = st.secrets["stats"]["password"]
    except Exception:
        st.error("Ajoutez `[stats] password = \"...\"` dans les secrets pour ouvrir cette page.")
        return False
    if st.session_state.get("stats_unlocked"):
        return True
    password = st.text_input("Mot de passe", type="password")
    if password and hmac.compare_digest(password, expected):
        st.session_state.stats_unlocked = True
        st.rerun()
    elif password:
        st.error("Mot de passe incorrect.")
    return False


@st.cache_data(ttl=300, show_spinner="Chargement des statistiques...")
def events(book: int) -> pd.DataFrame:
    return pd.DataFrame(load_events(book), columns=["game_id", "event", "page", "data", "created_at"])


def item_label(item) -> str:
    """L'objet de départ n°9 est une somme d'argent (cf. STARTING_ITEM_TABLE)."""
    return f"{item} Couronnes" if isinstance(item, int) else item


def table(rows: pd.DataFrame, percent: tuple = ()) -> None:
    """Tableau de chiffres, sans index ; les colonnes `percent` sont affichées en pourcentage."""
    st.dataframe(
        rows.reset_index(),
        hide_index=True,
        width="stretch",
        column_config={column: st.column_config.NumberColumn(format="percent") for column in percent},
    )


def counts(values: pd.Series, every: list, label: str) -> pd.DataFrame:
    """Nombre de sélections de chaque élément de `every`, y compris ceux jamais choisis."""
    frame = values.value_counts().reindex(every, fill_value=0).rename("sélections").to_frame()
    return frame.rename_axis(label).sort_values("sélections", ascending=False, kind="stable")


if not check_password():
    st.stop()

if st.button("🔄 Rafraîchir"):
    events.clear()

book = st.selectbox("Tome", list(BOOKS), format_func=lambda n: f"Tome {n} — {BOOKS[n]['title']}")
final_page = BOOKS[book]["final_page"]
df = events(book)
if df.empty:
    st.info("Aucune partie enregistrée pour l'instant.")
    st.stop()

starts = df[df.event == "start"]
pages = df[df.event == "page"].astype({"page": int})
deaths = df[df.event == "death"].astype({"page": int})
victories = df[df.event == "victory"]

# Issue de chaque partie : victoire, mort, ou ni l'un ni l'autre (en cours ou abandonnée)
games = pd.DataFrame(index=df.game_id.unique())
games["outcome"] = "En cours / abandon"
games.loc[games.index.isin(deaths.game_id), "outcome"] = "Mort"
games.loc[games.index.isin(victories.game_id), "outcome"] = "Victoire"
games["pages"] = pages.groupby("game_id").size().reindex(games.index, fill_value=0)

# --- Vue d'ensemble ------------------------------------------------------------------
total = len(games)
outcomes = games.outcome.value_counts()
col1, col2, col3, col4 = st.columns(4)
col1.metric("Parties", total)
col2.metric("Victoires", outcomes.get("Victoire", 0), f"{outcomes.get('Victoire', 0) / total:.0%} des parties", delta_color="off", delta_arrow="off")
col3.metric("Morts", outcomes.get("Mort", 0), f"{outcomes.get('Mort', 0) / total:.0%} des parties", delta_color="off", delta_arrow="off")
col4.metric("En cours / abandons", outcomes.get("En cours / abandon", 0))

finished = games[games.outcome != "En cours / abandon"]
winners = games[games.outcome == "Victoire"]
col1, col2, col3, col4 = st.columns(4)
col1.metric("Paragraphes par partie terminée", f"{finished.pages.mean():.0f}" if len(finished) else "—")
col2.metric("Paragraphes pour gagner", f"{winners.pages.mean():.0f}" if len(winners) else "—",
            f"de {winners.pages.min()} à {winners.pages.max()}" if len(winners) else None, delta_color="off", delta_arrow="off")
heroes = pd.json_normalize(starts.data.tolist()).assign(game_id=starts.game_id.values)
if not heroes.empty:
    heroes["outcome"] = heroes.game_id.map(games.outcome)
    col3.metric("HABILETÉ moyenne", f"{heroes.hability.mean():.1f}")
    won = heroes[heroes.outcome == "Victoire"]
    col4.metric("HABILETÉ moyenne des vainqueurs", f"{won.hability.mean():.1f}" if len(won) else "—")

st.divider()

# --- Disciplines Kaï -----------------------------------------------------------------
if not heroes.empty:
    disciplines = heroes[["game_id", "kai", "outcome"]].explode("kai")
    st.subheader("Disciplines Kaï")
    kai = counts(disciplines.kai, list(KAI), "Discipline")
    kai["% des parties"] = kai["sélections"] / len(heroes)
    kai["victoires"] = disciplines[disciplines.outcome == "Victoire"].kai.value_counts().reindex(kai.index, fill_value=0)
    kai["morts"] = disciplines[disciplines.outcome == "Mort"].kai.value_counts().reindex(kai.index, fill_value=0)
    # une Discipline jamais choisie n'a pas de taux de victoire : « — » plutôt que « None »
    kai["taux de victoire"] = [
        f"{won / chosen:.0%}" if chosen else "—" for won, chosen in zip(kai.victoires, kai["sélections"])
    ]
    table(kai, percent=("% des parties",))

    left, right = st.columns(2)
    with left:
        st.subheader("Armes maîtrisées")
        weapons = sorted(set(WEAPON_MASTERY_TABLE))
        table(counts(heroes.weapon_mastery.explode().dropna(), weapons, "Arme"))
    with right:
        if book == 1:
            st.subheader("Objet de départ")
            items = [item_label(item) for item in STARTING_ITEM_TABLE.values()]
            table(counts(heroes.starting_item.map(item_label), items, "Objet"))
    st.divider()

# --- Paragraphes ---------------------------------------------------------------------
visits = pd.concat([pages, deaths]).drop_duplicates(["game_id", "page"]).groupby("page").size()
never = sorted(set(range(1, final_page + 1)) - set(visits.index.astype(int)))
st.metric("Paragraphes visités", f"{final_page - len(never)} / {final_page}")
left, right = st.columns(2)
with left:
    st.subheader("Paragraphes les plus meurtriers")
    if len(deaths):
        death_counts = deaths.groupby("page").size()
        rates = pd.DataFrame({"morts": death_counts, "passages": visits.reindex(death_counts.index)})
        rates["taux de mort"] = rates.morts / rates.passages
        table(rates.sort_values("morts", ascending=False).rename_axis("paragraphe"), percent=("taux de mort",))
    else:
        st.caption("Aucune mort enregistrée.")
with right:
    st.subheader("Paragraphes les plus visités")
    table(visits.sort_values(ascending=False).head(30).rename("passages").to_frame().rename_axis("paragraphe"))
with st.expander(f"Paragraphes jamais visités ({len(never)})"):
    st.write(", ".join(map(str, never)) or "Aucun")
