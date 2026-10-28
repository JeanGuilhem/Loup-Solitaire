import streamlit as st
from combat import combat
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=343, book=3)

fr_text = """
L'étroitesse de la cellule interdit à vos adversaires de vous
attaquer tous en même temps. Vous devrez donc les combattre
un par un en respectant l'ordre dans lequel ils sont disposés ci-
dessous. Il est à noter que le Barbare des Glaces est insensible à
la Discipline Kaï de la Puissance Psychique.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat(
        [("Premier LOUP MAUDIT", 15, 24), ("Deuxième LOUP MAUDIT", 14, 23), ("Troisième LOUP MAUDIT", 14, 20)],
        key="loups",
    )
    if outcome == "win":
        st.write_stream(stream_text("Les trois Loups Maudits sont morts. Il vous faut maintenant affronter le Barbare des Glaces, insensible à votre Puissance Psychique."))
        outcome_barbare = combat([("BARBARE DES GLACES", 17, 29)], key="barbare", psychic_immune=True)
        if outcome_barbare == "win":
            st.write_stream(stream_text("Si vous sortez vainqueur de ce quadruple combat, rendez-vous au :"))
            st.page_link("tomes/tome3/page_28.py", label="28", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
