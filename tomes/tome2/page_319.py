import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=319, book=2)

fr_text = """
La rue aboutit soudain à une grande tour de guet aux murs de pierre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez entrer dans la tour, rendez-vous au :"))
    st.page_link("tomes/tome2/page_271.py", label="271", icon="📄")
    st.write_stream(stream_text("Si vous préférez retourner dans la taverne, rendez-vous au :"))
    st.page_link("tomes/tome2/page_177.py", label="177", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
