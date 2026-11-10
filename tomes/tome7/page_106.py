import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, ls_death

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=106, book=7)

fr_text = """
Vous n'êtes plus qu'à quelques mètres de l'entrée du tunnel ouest
lorsque, soudain, une douleur fulgurante vous frappe en plein
dos, puis explose dans votre poitrine comme une boule de feu.
Vous chancelez et tombez à terre, le corps pratiquement coupé
en deux par cette terrifiante décharge d'énergie destructrice. La
mort est instantanée. Le bâton magique d'un Dhax vient de
mettre un terme à votre aventure.
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
