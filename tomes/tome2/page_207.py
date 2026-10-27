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

check_inventory(current_page_number=207, book=2)

fr_text = """
Moins de 100 mètres plus loin, le sentier s'arrête au bord d'un précipice.
Les eaux du chenal de Ryner coulent au-dessous et il est impossible
d'aller plus loin. Il ne vous reste donc plus qu'à rebrousser chemin et à
prendre le pont qui traverse le chenal.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome2/page_47.py", label="47", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
