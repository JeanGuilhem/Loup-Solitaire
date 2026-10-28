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

check_inventory(current_page_number=297, book=3)

fr_text = """
Au bout de cinq minutes de marche environ, le couloir tourne
brusquement en direction du nord. Un peu plus loin sur votre
gauche, vous apercevez une grande porte de pierre ; le levier fixé
au mur, juste à côté, est en position haute et la porte fermée.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez tirer ce levier et ouvrir la porte, rendez-vous au :'))
    st.page_link("tomes/tome3/page_317.py", label="317", icon="📄")

    st.write_stream(stream_text('Si vous préférez poursuivre votre chemin en direction du nord, rendez-vous au :'))
    st.page_link("tomes/tome3/page_126.py", label="126", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
