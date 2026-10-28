import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies, ls_death

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=136, book=3)

fr_text = """
Soudain, vous êtes projeté en arrière tandis que le pont de glace
commence à se disloquer. Pendant quelques secondes, le
traîneau reste en équilibre instable sur le bord, comme une
balançoire, et vous entendez les cris d'horreur de vos guides
impuissants à vous venir en aide. C'est d'ailleurs là le dernier son
que vous entendrez jamais, car le pont s'effondre et vous
précipite dans le gouffre. Vous faites une chute de 600 mètres au
terme de laquelle vous êtes, bien entendu, tué sur le coup. Votre
mission s'achève donc ici en même temps que votre vie.
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
