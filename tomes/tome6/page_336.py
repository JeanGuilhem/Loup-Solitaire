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

check_inventory(current_page_number=336, book=6)

fr_text = """
Vous vous frayez un chemin à travers la foule bruyante des
soldats et vous finissez par atteindre un petit coin écarté à l'autre
bout du comptoir.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez parler à l'une des serveuses, rendez-vous au :"))
    st.page_link("tomes/tome6/page_299.py", label="299", icon="📄")

    st.write_stream(stream_text('Si vous voulez vous attabler, rendez-vous au :'))
    st.page_link("tomes/tome6/page_316.py", label="316", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
