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

check_inventory(current_page_number=288, book=2)

fr_text = """
Sans prononcer un mot, le chevalier vous montre du doigt la forêt qui
s'étend derrière vous et rentre à l'intérieur de la tour, dont il referme la
porte à clé. C'est une forêt touffue où s'enchevêtrent parmi les arbres de
hautes herbes et des buissons d'épines. Il est inutile d'essayer de la
traverser à cheval et il ne vous reste donc plus qu'à abandonner votre
monture pour continuer votre chemin à pied.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome2/page_244.py", label="244", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
