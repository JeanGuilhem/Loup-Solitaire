import streamlit as st
from combat import combat
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=68, book=3)

fr_text = """
Le Barbare des Glaces s'approche et soudain, il pousse un cri à
vous figer le sang, puis se précipite sur vous.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("BARBARE DES GLACES", 18, 28)])
    if outcome == "win":

        st.write_stream(stream_text('Si vous sortez vainqueur de ce combat, rendez-vous au :'))
        st.page_link("tomes/tome3/page_186.py", label="186", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
