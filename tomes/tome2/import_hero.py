"""
Recréer à la main le héros qui a terminé le tome 1 (sauvegarde perdue, partie jouée ailleurs...),
puis l'envoyer à la page de départ du tome 2 comme s'il venait du paragraphe 350.
"""
import streamlit as st

from inventory import add_to_inventory, reset_state
from variable import BOOK2_EQUIPMENT, ITEMS, KAI, MAX_BACKPACK, MAX_PURSE, MAX_WEAPONS, WEAPON_MASTERY_TABLE

WEAPON_MASTERY = "La Maîtrise des armes"
PREVIOUS_BOOK_DISCIPLINES = 5
RECREATED = "Tome 1 (héros recréé à partir de sa Feuille d'Aventure)."

st.set_page_config(page_title="Recréer mon héros", page_icon="📝")
st.title("📝 Recréer mon héros du tome 1")
st.write(
    "Recopiez votre Feuille d'Aventure telle qu'elle était à la fin du tome 1. "
    "Indiquez l'HABILETÉ et l'ENDURANCE **de base** (sans le Casque ni la Cotte de Mailles : "
    "leurs bonus sont ajoutés automatiquement)."
)


def items_of(kind: str) -> list:
    """Objets du catalogue d'un type donné, sauf ceux reçus au début du tome 2."""
    return [
        name for name, info in ITEMS.items()
        if info["type"] == kind and name not in BOOK2_EQUIPMENT["special"]
    ]


col1, col2, col3 = st.columns(3)
hability = col1.number_input("Habileté de base", min_value=10, max_value=19, value=15)
endurance = col2.number_input("Endurance de base", min_value=20, max_value=29, value=25)
purse = col3.number_input("Couronnes", min_value=0, max_value=MAX_PURSE, value=0)

kai = st.multiselect(
    f"Vos {PREVIOUS_BOOK_DISCIPLINES} Disciplines Kaï",
    list(KAI),
    max_selections=PREVIOUS_BOOK_DISCIPLINES,
)
mastered = None
if WEAPON_MASTERY in kai:
    mastered = st.selectbox("Arme maîtrisée", sorted(set(WEAPON_MASTERY_TABLE)))

weapons = st.multiselect("Armes", items_of("weapon"), max_selections=MAX_WEAPONS)
has_backpack = st.checkbox("J'ai toujours mon Sac à Dos", value=True)
meals, backpack = 0, []
if has_backpack:
    col1, col2 = st.columns([1, 3])
    meals = col1.number_input("Repas", min_value=0, max_value=MAX_BACKPACK, value=0)
    backpack = col2.multiselect(
        "Autres objets du Sac à Dos", [item for item in items_of("backpack") if item != "REPAS"]
    )
special = st.multiselect("Objets Spéciaux", items_of("special"))

problems = []
if len(kai) != PREVIOUS_BOOK_DISCIPLINES:
    problems.append(f"choisissez exactement {PREVIOUS_BOOK_DISCIPLINES} Disciplines Kaï")
if meals + len(backpack) > MAX_BACKPACK:
    problems.append(f"le Sac à Dos ne peut contenir que {MAX_BACKPACK} objets (Repas compris)")
if problems:
    st.info("Pour valider : " + " ; ".join(problems) + ".")

if st.button("Valider mon héros", type="primary", disabled=bool(problems)):
    reset_state()
    st.session_state.hability = int(hability)
    st.session_state.total_endurance = st.session_state.endurance = int(endurance)
    st.session_state.purse = int(purse)
    st.session_state.kai = list(kai)
    st.session_state.weapon_mastery = [mastered] if mastered else []
    st.session_state.has_backpack = has_backpack
    for item in weapons + backpack + special:
        add_to_inventory(item, origin=RECREATED)  # les bonus d'ENDURANCE des Objets Spéciaux sont appliqués ici
    if meals:
        add_to_inventory("REPAS", quantity=int(meals), origin=RECREATED)
    # comme un héros qui vient d'atteindre le paragraphe 350 du tome 1
    st.session_state.book = 1
    st.session_state.completed_books = [1]
    st.session_state.current_page_number = 350
    st.session_state.game_phase = "playing"
    st.session_state.transition = "import"
    st.switch_page("tomes/tome2/debut.py")

st.page_link("tomes/tome2/debut.py", label="Retour", icon="↩️")
