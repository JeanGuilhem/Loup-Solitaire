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

check_inventory(current_page_number=340, book=2)

fr_text = """
Vous continuez de marcher pendant encore une demi-heure le long du
tunnel avant d'arriver à une bifurcation.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez prendre la voie de gauche, rendez-vous au :"))
    st.page_link("tomes/tome2/page_64.py", label="64", icon="📄")
    st.write_stream(stream_text("Si vous préférez emprunter la voie de droite, rendez-vous au :"))
    st.page_link("tomes/tome2/page_164.py", label="164", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
