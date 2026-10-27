import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import stream_text, called_cookies, ls_death

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=190, book=2)

fr_text = """
Vous vous servez d'une règle de fer comme d'un levier pour forcer la
serrure et vous ressentez soudain une douleur cuisante dans la poitrine.
Le coffret comportait un piège : une petite aiguille enduite de poison
qui vient de se planter dans votre chair tandis que vous tentiez de faire
sauter la serrure. Cette minuscule fléchette vous est fatale et vous
mourez sur le coup. Votre mission s'achève ici, en même temps que
votre vie.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    show_illustrations()
    ls_death()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
