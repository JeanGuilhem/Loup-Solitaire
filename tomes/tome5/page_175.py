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

check_inventory(current_page_number=175, book=5)

fr_text = """
Avant que vous ne trouviez une cachette adéquate, trois
Sharnazims surgissent : « Laissez-le-moi, bande d'imbéciles ! »
hurle une voix rauque. Les Gardes s'écartent pour laisser passer
Maouk, qui surgit de l'ombre en brandissant une fléchette. Il
laisse échapper un juron puis lance sa flèche en visant votre
poitrine.
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
