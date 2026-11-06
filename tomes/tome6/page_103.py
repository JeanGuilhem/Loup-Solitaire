import streamlit as st
from inventory import (
    check_inventory,
    clear_flag,
    display_inventory,
    end_page,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=103, book=6)

fr_text = """
Malheureusement, votre score est trop faible pour vous qualifier
pour la seconde partie du tournoi, et l'on vous demande poliment
de bien vouloir quitter le terrain. Si vous avez emprunté un
arc, allez le rendre avant de partir rejoindre Cyrilus.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # l'arc emprunté pour le tournoi (faits « arc emprunté », « arc Jakan », « arc de Kalte ») est rendu
    if is_new_page():
        for flag in ("arc emprunté", "arc Jakan", "arc de Kalte"):
            clear_flag(flag)

    st.write_stream(stream_text("Ensuite, rendez-vous au :"))
    st.page_link("tomes/tome6/page_33.py", label="33", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
