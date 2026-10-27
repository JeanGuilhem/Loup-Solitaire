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

check_inventory(current_page_number=293, book=2)

fr_text = """
Cette route mène à une cabane abandonnée. L'intérieur en est garni de
meubles recouverts d'une bonne couche de poussière. De toute
évidence, il y a plusieurs mois que personne n'y est entré. La route ne
va pas plus loin, c'est un cul-de-sac et vous vous rendez compte à cet
instant que vous venez de perdre un temps précieux. Il ne vous reste
plus qu'à rebrousser chemin jusqu'à la bifurcation et à prendre la voie
de gauche.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Hâtez-vous de vous rendre au :'))
    st.page_link("tomes/tome2/page_155.py", label="155", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
