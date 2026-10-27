"""
Départ du tome 2, « La Traversée Infernale ». Trois façons d'arriver ici :
    continue : le héros vient de finir le tome 1 (paragraphe 350, ou sauvegarde) ;
    import   : le joueur a recréé à la main son héros du tome 1 (import_hero.py) ;
    new      : un nouveau héros vient d'être créé pour le tome 2 (crafting_hero.py).
Les deux premiers gardent tout et choisissent une 6e Discipline Kaï. Tous retrouvent leur
ENDURANCE maximale et reçoivent l'équipement du tome 2 (cf. BOOK2_EQUIPMENT).
"""
import streamlit as st

from game_stats import record_start
from inventory import (
    add_gold,
    add_to_inventory,
    display_inventory,
    has_item,
    init_state,
    item_info,
    remove_from_inventory,
)
from save import apply_save, read_save
from utils import table_des_hasards
from variable import (
    BOOK2_EQUIPMENT,
    BOOKS,
    KAI,
    MAX_BACKPACK,
    MAX_PURSE,
    MAX_WEAPONS,
    WEAPON_MASTERY_TABLE,
)

BOOK = 2
WEAPON_MASTERY = "La Maîtrise des armes"
ARSENAL = "Tome 2 : Arsenal du Palais de Holmgard, avant le départ pour Durenor."
GIVEN_BY_KING = "Tome 2 : confié par le roi du Sommerlund pour obtenir l'aide de Durenor."

st.set_page_config(page_title=f"Tome {BOOK}", page_icon="📜")
st.title(f"📜 Tome {BOOK} — {BOOKS[BOOK]['title']}")


def has_finished_book_1(state) -> bool:
    return (
        state.get("hability", 0) > 0
        and 1 in (state.get("completed_books") or [])
        and state.get("book", 1) == 1
    )


def transition_mode():
    """Comment le héros arrive au tome 2 (cf. docstring), ou None s'il n'a pas encore de héros."""
    mode = st.session_state.get("transition")
    if mode is None:
        if has_finished_book_1(st.session_state):
            mode = "continue"
        elif (
            st.session_state.get("game_phase") == "creation"
            and st.session_state.get("creation_book") == BOOK
            and st.session_state.get("kai")
        ):
            mode = "new"
        else:
            return None
        st.session_state.transition = mode
    return mode


def choose_hero() -> None:
    """Pas de héros prêt pour le tome 2 : reprendre celui de la sauvegarde, le recréer, ou en créer un."""
    saved = read_save()
    if saved == "pending":
        st.info("Chargement de votre sauvegarde...")
        st.stop()

    if isinstance(saved, dict) and has_finished_book_1(saved):
        st.success("Votre héros a terminé le tome 1 : il peut poursuivre l'aventure.")
        if st.button("Continuer avec mon héros du tome 1", icon="🐺", type="primary"):
            init_state()
            apply_save(saved)
            st.rerun()
        st.divider()

    st.write(
        "Pour partir à Durenor, il vous faut un héros. Si vous avez terminé le tome 1 ailleurs "
        "ou perdu votre sauvegarde, recréez votre Loup Solitaire tel qu'il était à la fin du tome 1. "
        "Sinon, créez un nouveau héros."
    )
    if isinstance(saved, dict) and not has_finished_book_1(saved):
        st.warning("Votre partie en cours sera effacée.")
    col1, col2 = st.columns(2)
    col1.page_link("tomes/tome2/import_hero.py", label="Recréer mon héros du tome 1", icon="📝")
    if col2.button("Créer un nouveau héros", icon="⚔️"):
        st.session_state.creation_request = BOOK
        st.session_state.game_phase = None
        st.switch_page("tomes/tome1/crafting_hero.py")
    st.stop()


def show_hero() -> None:
    col1, col2, col3 = st.columns(3)
    col1.metric("Habileté", st.session_state.hability)
    col2.metric("Endurance", f"{st.session_state.endurance}/{st.session_state.total_endurance}")
    col3.metric("Couronnes", f"{st.session_state.purse}/{MAX_PURSE}")
    st.write("**Disciplines Kaï :** " + ", ".join(st.session_state.kai))
    if st.session_state.weapon_mastery:
        st.write(f"**Arme maîtrisée :** {st.session_state.weapon_mastery[0]}")


def choose_new_discipline() -> bool:
    """Le héros venu du tome 1 ajoute une 6e Discipline Kaï. Renvoie True une fois choisie."""
    if "new_kai" in st.session_state:
        st.write(f"Nouvelle Discipline Kaï : **{st.session_state.new_kai}**")
        if st.session_state.new_kai == WEAPON_MASTERY:
            st.write(
                f"*Vous avez tiré le {st.session_state.weapon_mastery_roll}* : vous maîtrisez "
                f"cette arme : **{st.session_state.weapon_mastery[0]}**"
            )
        return True

    st.write(
        "Votre maîtrise des arts Kaï a progressé au cours de votre première mission : "
        "choisissez une nouvelle Discipline Kaï."
    )
    choices = [name for name in KAI if name not in st.session_state.kai]
    choice = st.selectbox("Nouvelle Discipline Kaï", choices)
    st.caption(KAI[choice].strip())
    if st.button("Valider ma nouvelle Discipline", type="primary"):
        st.session_state.kai.append(choice)
        st.session_state.new_kai = choice
        if choice == WEAPON_MASTERY:
            st.session_state.weapon_mastery_roll = table_des_hasards() % 10
            st.session_state.weapon_mastery = [WEAPON_MASTERY_TABLE[st.session_state.weapon_mastery_roll]]
        st.rerun()
    return False


def item_label(item: str) -> str:
    return "2 REPAS" if item == "REPAS" else item


def receive_equipment() -> bool:
    """Couronnes (10 + Table de Hasard) et objets au choix du tome 2. Renvoie True une fois reçus."""
    if "book2_gold_roll" not in st.session_state:
        if st.button("Recevoir votre bourse", icon="💰", type="primary"):
            st.session_state.book2_gold_roll = table_des_hasards() % 10
            add_gold(BOOK2_EQUIPMENT["gold_base"] + st.session_state.book2_gold_roll)
            st.rerun()
        return False
    gold = BOOK2_EQUIPMENT["gold_base"] + st.session_state.book2_gold_roll
    st.write(f"*Vous avez tiré le {st.session_state.book2_gold_roll}* : vous recevez **{gold} Couronnes**.")

    if "book2_items" in st.session_state:
        st.write("Vous avez choisi : **" + ", ".join(map(item_label, st.session_state.book2_items)) + "**.")
        return True

    count = BOOK2_EQUIPMENT["items_to_choose"]
    chosen = st.multiselect(
        f"Choisissez {count} objets",
        BOOK2_EQUIPMENT["items"],
        format_func=item_label,
        max_selections=count,
    )
    weapons = sum(1 for item in chosen if item_info(item)["type"] == "weapon")
    backpack = sum(2 if item == "REPAS" else 1 for item in chosen if item_info(item)["type"] == "backpack")
    problems = []

    # « vous avez là l'occasion d'échanger l'une [de vos armes] ou les deux »
    current_weapons = list(st.session_state.weapons)
    excess = len(current_weapons) + weapons - MAX_WEAPONS
    left_behind = []  # positions dans current_weapons
    if excess == 1:
        left_behind = [
            st.radio(
                f"Vous ne pouvez porter que {MAX_WEAPONS} armes : laquelle laissez-vous à l'Arsenal "
                "en échange ?",
                range(len(current_weapons)),
                format_func=lambda index: current_weapons[index],
            )
        ]
    elif excess > 1:
        left_behind = list(range(len(current_weapons)))
        st.info(
            "Vous laissez à l'Arsenal vos armes actuelles en échange : "
            + ", ".join(current_weapons) + "."
        )
    if backpack and not st.session_state.has_backpack:
        problems.append("vous n'avez plus de Sac à Dos")
    elif len(st.session_state.backpack) + backpack > MAX_BACKPACK:
        problems.append(f"votre Sac à Dos ne peut contenir que {MAX_BACKPACK} objets")
    if problems:
        st.warning(
            "Pas assez de place : " + " et ".join(problems)
            + ". Vous pouvez aussi jeter des objets depuis votre inventaire ci-dessous, "
            "ou choisir d'autres objets."
        )
    if st.button("Prendre ces objets", disabled=len(chosen) != count or bool(problems)):
        for weapon in [current_weapons[index] for index in left_behind]:
            remove_from_inventory(weapon)
        for item in chosen:
            add_to_inventory(item, quantity=2 if item == "REPAS" else 1, origin=ARSENAL)
        for item in BOOK2_EQUIPMENT["special"]:
            if not has_item(item):
                add_to_inventory(item, origin=GIVEN_BY_KING if item == "SCEAU D'HAMMARDAL" else ARSENAL)
        st.session_state.book2_items = chosen
        st.rerun()
    return False


def start_book() -> None:
    """Le héros part pour le paragraphe d'introduction du tome 2 : nouvelle partie pour les statistiques."""
    mode = st.session_state.transition
    st.session_state.book = BOOK
    st.session_state.current_page_number = 0
    st.session_state.last_page_number = 0
    st.session_state.game_phase = "playing"
    record_start(continued=mode != "new", items=st.session_state.book2_items)
    for key in ("transition", "creation_book", "endurance_restored", "new_kai", "book2_gold_roll", "book2_items"):
        st.session_state.pop(key, None)
    st.switch_page(f"tomes/tome{BOOK}/pages_intro.py")


mode = transition_mode()
if mode is None:
    choose_hero()

if not st.session_state.get("endurance_restored"):
    # chaque tome commence avec l'ENDURANCE au maximum
    st.session_state.endurance = st.session_state.total_endurance
    st.session_state.endurance_restored = True

st.subheader("Votre héros")
show_hero()
st.divider()

if mode in ("continue", "import"):
    st.subheader("Une nouvelle Discipline Kaï")
    if not choose_new_discipline():
        st.stop()
    st.divider()

st.subheader("Votre équipement")
if receive_equipment():
    st.divider()
    if st.button("Partir pour Durenor", icon="📜", type="primary"):
        start_book()

with st.expander("Afficher mon inventaire"):
    display_inventory()
