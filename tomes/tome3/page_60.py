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

check_inventory(current_page_number=60, book=3)

fr_text = """
Vous avez à peine monté une douzaine de marches qu'un éclair
aveuglant jaillit entre les deux piliers. Vous voyez alors la Statue
remuer, comme animée par une soudaine énergie.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez attaquer cette créature avant qu'elle ne se dresse sur l'autel, rendez-vous au :"))
    st.page_link("tomes/tome3/page_150.py", label="150", icon="📄")

    st.write_stream(stream_text('Si vous préférez rester parfaitement immobile et vous préparer à combattre, rendez-vous au :'))
    st.page_link("tomes/tome3/page_31.py", label="31", icon="📄")

    st.write_stream(stream_text("Enfin, si vous estimez plus sage de vous précipiter vers l'arcade obscure, rendez-vous au :"))
    st.page_link("tomes/tome3/page_306.py", label="306", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
