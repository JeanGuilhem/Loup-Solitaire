"""
Recréer à la main le héros qui a terminé le tome précédent (sauvegarde perdue, partie jouée
ailleurs...), puis l'envoyer à la page de départ du tome comme s'il venait du dernier paragraphe.
tomes/tome<N>/import_hero.py appelle import_hero(N).
"""
import streamlit as st

from inventory import add_to_inventory, reset_state
from kai_cards import choose_disciplines
from variable import (
    BOOK_EQUIPMENT,
    BOOKS,
    ITEMS,
    KAI,
    MAX_BACKPACK,
    MAX_PURSE,
    MAX_WEAPONS,
    WEAPON_MASTERY_TABLE,
)

WEAPON_MASTERY = "La Maîtrise des armes"


def items_of(kind: str, book: int) -> list:
    """Objets du catalogue d'un type donné, sauf ceux remis d'office au début du tome."""
    return [
        name for name, info in ITEMS.items()
        if info["type"] == kind and name not in BOOK_EQUIPMENT[book]["special"]
    ]


def import_hero(book: int) -> None:
    previous = book - 1
    disciplines = 5 + previous - 1  # 5 au tome 1, une de plus par tome terminé
    origin = f"Tome {previous} (héros recréé à partir de sa Feuille d'Aventure)."

    st.set_page_config(page_title="Recréer mon héros", page_icon="📝")
    st.title(f"📝 Recréer mon héros du tome {previous}")
    st.write(
        f"Recopiez votre Feuille d'Aventure telle qu'elle était à la fin du tome {previous}. "
        "Indiquez l'HABILETÉ et l'ENDURANCE **de base** (sans le Casque, la Cotte de Mailles ni les "
        "autres Objets Spéciaux : leurs bonus sont ajoutés automatiquement)."
    )

    col1, col2, col3 = st.columns(3)
    hability = col1.number_input("Habileté de base", min_value=10, max_value=19, value=15)
    endurance = col2.number_input("Endurance de base", min_value=20, max_value=29, value=25)
    purse = col3.number_input("Couronnes", min_value=0, max_value=MAX_PURSE, value=0)

    st.write(f"Vos {disciplines} Disciplines Kaï :")
    kai = choose_disciplines(list(KAI), disciplines, key="import_kai_cards")
    mastered = None
    if WEAPON_MASTERY in kai:
        mastered = st.selectbox("Arme maîtrisée", sorted(set(WEAPON_MASTERY_TABLE)))

    weapons = st.multiselect(
        "Armes", items_of("weapon", book), max_selections=MAX_WEAPONS, placeholder="Choisir des armes"
    )
    has_backpack = st.checkbox("J'ai toujours mon Sac à Dos", value=True)
    meals, backpack = 0, []
    if has_backpack:
        col1, col2 = st.columns([1, 3])
        meals = col1.number_input("Repas", min_value=0, max_value=MAX_BACKPACK, value=0)
        backpack = col2.multiselect(
            "Autres objets du Sac à Dos", [item for item in items_of("backpack", book) if item != "REPAS"],
            placeholder="Choisir des objets",
        )
    special = st.multiselect(
        "Objets Spéciaux", items_of("special", book), placeholder="Choisir des Objets Spéciaux"
    )

    problems = []
    if len(kai) != disciplines:
        problems.append(f"choisissez exactement {disciplines} Disciplines Kaï")
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
        # les objets sont rangés comme au tome précédent (places dans le Sac à Dos)
        st.session_state.book = previous
        for item in weapons + backpack + special:
            add_to_inventory(item, origin=origin)  # les bonus d'ENDURANCE des Objets Spéciaux sont appliqués ici
        if meals:
            add_to_inventory("REPAS", quantity=int(meals), origin=origin)
        # comme un héros qui vient d'atteindre le dernier paragraphe du tome précédent
        st.session_state.completed_books = list(range(1, book))
        st.session_state.current_page_number = BOOKS[previous]["final_page"]
        st.session_state.game_phase = "playing"
        st.session_state.transition = "import"
        st.switch_page(f"tomes/tome{book}/debut.py")

    st.page_link(f"tomes/tome{book}/debut.py", label="Retour", icon="↩️")
