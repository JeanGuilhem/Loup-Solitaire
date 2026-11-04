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

check_inventory(current_page_number=99, book=5)

fr_text = """
Alors que vous ressortez à l'air libre, une voix forte s'élève
soudain des bruits de la foule : « Le voilà ! » Il s'agit de Maouk,
qui vous désigne du doigt tandis qu'une douzaine de Sharnazims
dégainent leurs cimeterres. « Rendez-vous, Loup Solitaire !
reprend Maouk. Cette fois, vous ne vous échapperez pas. »
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez vous battre, rendez-vous au :"))
    st.page_link("tomes/tome5/page_36.py", label="36", icon="📄")

    st.write_stream(stream_text("Si vous préférez vous rendre, rendez-vous au :"))
    st.page_link("tomes/tome5/page_176.py", label="176", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
