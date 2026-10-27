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

check_inventory(current_page_number=227, book=2)

fr_text = """
Quatre gardes de la ville, armés de pied en cap, marchent au milieu de
la rue. Vous ne voulez pas courir le risque d'être interpellé et vous vous
réfugiez dans une ruelle à votre gauche. Mais les soldats s'immobilisent
juste à l'entrée du passage et il suffirait que l'un d'eux tourne la tête
pour que vous soyez immédiatement repéré. Derrière vous, une petite
fenêtre ouverte vous permet de distinguer l'intérieur d'une taverne
bondée. Sans la moindre hésitation, vous enjambez aussitôt le rebord de
la fenêtre et vous entrez à l'intérieur.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome2/page_4.py", label="4", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
