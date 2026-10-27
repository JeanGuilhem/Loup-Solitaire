import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=335, book=2)

fr_text = """
Vous remarquez une enseigne accrochée à la façade d'une petite
boutique :

KLASPAR — ASTRONOME ET SAGE
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez entrer dans cette boutique et y demander votre chemin pour Durenor, rendez-vous au :"))
    st.page_link("tomes/tome2/page_161.py", label="161", icon="📄")
    st.write_stream(stream_text("Si vous préférez continuer tout droit, rendez-vous au :"))
    st.page_link("tomes/tome2/page_61.py", label="61", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
