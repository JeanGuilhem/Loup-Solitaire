import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import ls_death, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=9, book=3)

fr_text = """
Vous essayez désespérément de lutter contre l'atroce douleur,
mais elle est si intense que vous perdez bientôt conscience. Dans
quelques minutes, vous serez complètement vidé de votre
énergie et vous deviendrez l'esclave docile de Vonotar, incapable
de résister au pouvoir de sa force psychique ; il vous ordonnera
alors de ramasser l'épée du Barbare des Glaces et de vous en
servir pour vous trancher la gorge. Vous obéirez sans murmure et
vous vous tuerez vous-même d'un simple geste du poignet. Votre
mission s'achèvera donc ici en même temps que votre vie.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    show_illustrations()
    ls_death()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
