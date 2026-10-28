import streamlit as st
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

check_inventory(current_page_number=268, book=3)

fr_text = """
Vous parvenez à briser la cire sans casser la fiole. Il ne vous reste
plus qu'à déboucher celle-ci: le liquide noir dégage alors une
odeur forte et âcre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous êtes déjà allé dans le Cimetière des Anciens (au cours de votre première aventure), rendez-vous au :'))
    st.page_link("tomes/tome3/page_177.py", label="177", icon="📄")

    st.write_stream(stream_text('Sinon, vous vous hâtez de reboucher la fiole. Cette odeur en effet vous donne la nausée et vous ne souhaitez pas conserver ce liquide douteux. Retournez au 10 et faites un nouveau choix :'))
    st.page_link("tomes/tome3/page_10.py", label="10", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
