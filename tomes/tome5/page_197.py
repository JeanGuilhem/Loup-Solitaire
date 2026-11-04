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

check_inventory(current_page_number=197, book=5)

fr_text = """
Maouk extrait de son habit une petite flèche qu'il tient serrée
dans son poing puissant. Il lève le bras puis lance la fléchette en
visant votre poitrine. Vous êtes à bout portant et vous ne pouvez
rien faire pour éviter le projectile. La flèche vous atteint en pleine
poitrine, vous coupant le souffle.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome5/page_25.py", label="25", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
