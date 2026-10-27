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

check_inventory(current_page_number=286, book=2)

fr_text = """
Vous tombez à la mer et vous nagez sous l'eau pendant plus d'une
minute pour éviter de recevoir sur la tête les brandons qui jaillissent des
navires enflammés ou les cadavres qu'on précipite par-dessus bord.
Lorsque le manque d'air vous oblige enfin à refaire surface, la vision
qui s'offre à vous fait renaître l'espoir d'une issue favorable.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome2/page_109.py", label="109", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
