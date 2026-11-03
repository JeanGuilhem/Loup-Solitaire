import streamlit as st
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

check_inventory(current_page_number=86, book=4)

fr_text = """
Vous bondissez sur un chariot renversé et vous apercevez en
même temps deux soldats qui, à l'aide de leurs tuniques,
étouffent les flammes des vêtements du capitaine Gayal. Vous
adressez des prières au ciel pour qu'il survive à ses brûlures et
qu'il soit encore temps de rassembler ses hommes dispersés.
L'ennemi a atteint le périmètre en ruines de Ruanon et poursuit
maintenant son avancée à l'abri des pans de murs encore debout.
Vous lancez des ordres aux hommes du capitaine Gayal pour
qu'ils reviennent en hâte vers la barricade. Vos adversaires
cependant ne sont plus qu'à une centaine de mètres. Est-il trop
tard pour repousser leur attaque ?
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome4/page_186.py", label="186", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
