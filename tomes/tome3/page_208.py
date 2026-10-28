import streamlit as st
from combat import combat
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

check_inventory(current_page_number=208, book=3)

fr_text = """
Le Barbare des Glaces vous voit approcher et tire aussitôt son
épée en os, puis il se poste devant l'escalier pour vous empêcher
de passer. Il vous faut l'affronter.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("BARBARE DES GLACES", 17, 30)])
    if outcome == "win":
        if st.session_state["combat_combat"]["round"] <= 4:
            st.write_stream(stream_text("Vous avez remporté la victoire en 4 Assauts ou moins, rendez-vous au :"))
            st.page_link("tomes/tome3/page_4.py", label="4", icon="📄")
        else:
            st.write_stream(stream_text("Vous avez gagné le combat en plus de 4 Assauts, rendez-vous au :"))
            st.page_link("tomes/tome3/page_81.py", label="81", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
