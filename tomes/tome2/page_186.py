import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=186, book=2)

fr_text = """
Vous arrivez bientôt devant un grand bâtiment qui porte cette
inscription sur sa façade :

**ÉCURIES DE RAGADORN — RELAIS DE DILIGENCE**

Un cocher vêtu d'un uniforme vert est assis près d'un tableau
d'affichage qui indique :

**Port Bax — Durée du voyage : 7 jours**
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez demander au cocher un billet pour Port Bax, rendez-vous au :"))
    st.page_link("tomes/tome2/page_136.py", label="136", icon="📄")

    st.write_stream(stream_text("Si vous n'avez pas d'argent, rendez-vous au :"))
    st.page_link("tomes/tome2/page_238.py", label="238", icon="📄", disabled=st.session_state.purse > 0)
    if st.session_state.purse > 0:
        st.caption("Vous avez encore de l'argent dans votre bourse.")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
