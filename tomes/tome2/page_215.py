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

check_inventory(current_page_number=215, book=2)

fr_text = """
Une trentaine de mètres plus loin, du côté gauche de la rue, des cris
joyeux et des chants filtrent à travers la façade d'une grande bâtisse
délabrée. Une enseigne rouillée grince au-dessus de la porte.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous voulez entrer dans la taverne, rendez-vous au :'))
    st.page_link("tomes/tome2/page_4.py", label="4", icon="📄")

    st.write_stream(stream_text('Si vous préférez continuer de marcher le long de la rue de la Bernicle, rendez-vous au :'))
    st.page_link("tomes/tome2/page_83.py", label="83", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
