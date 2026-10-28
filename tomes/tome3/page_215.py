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

check_inventory(current_page_number=215, book=3)

fr_text = """
Le couloir forme un angle et vous vous hâtez de tourner le coin.
Derrière vous, tout semble silencieux et vous poussez un soupir
de soulagement. Vous remarquez alors que le grondement
entendu précédemment est devenu plus intense dans ce tunnel.
A quelques mètres sur votre gauche, un petit passage mène à une
porte de pierre qui est fermée.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez examiner cette porte, rendez-vous au :"))
    st.page_link("tomes/tome3/page_13.py", label="13", icon="📄")
    st.write_stream(
        stream_text(
            "Si vous préférez poursuivre votre chemin le long du couloir en direction du nord, rendez-vous au "
            ":"
        )
    )
    st.page_link("tomes/tome3/page_254.py", label="254", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
