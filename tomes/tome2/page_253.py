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

check_inventory(current_page_number=253, book=2)

fr_text = """
La rue longe le mur du port en direction du fleuve Dorn ; au bord du
fleuve, elle tourne brusquement vers le sud et aboutit à la rue du Butin.
Vous passez devant les entrepôts alignés le long du quai et vous
reconnaissez un peu plus loin le poteau de pierre planté au milieu de la
place.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez poursuivre en direction du sud, rendez-vous au :'))
    st.page_link("tomes/tome2/page_303.py", label="303", icon="📄")

    st.write_stream(stream_text('Si vous préférez prendre la rue de la Bernicle et retourner à la taverne, rendez-vous au :'))
    st.page_link("tomes/tome2/page_177.py", label="177", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
