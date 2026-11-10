import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_magnakai,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=337, book=7)

fr_text = """
Le mur descend rapidement, et vous n'avez plus qu'un tout petit
espace par où vous enfuir.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    roll = hazard_roll(key="mur", label="Utilisez la Table de Hasard pour obtenir un chiffre. Si vous maîtrisez la Discipline Magnakaï de l'Art de la Chasse, ajoutez 3 au chiffre obtenu.")
    if roll is not None:
        bonus = 3 if has_magnakai("Art de la Chasse") else 0
        total = roll + bonus
        if bonus:
            st.write(f"*Art de la Chasse : {roll} + 3 = **{total}**.*")
        st.write_stream(stream_text("Si votre total est compris entre 0 et 4, rendez-vous au :"))
        st.page_link("tomes/tome7/page_237.py", label="237", icon="📄", disabled=total > 4)
        st.write_stream(stream_text("S'il est égal ou supérieur à 5, rendez-vous au :"))
        st.page_link("tomes/tome7/page_188.py", label="188", icon="📄", disabled=total <= 4)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
