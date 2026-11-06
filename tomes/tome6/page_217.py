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

check_inventory(current_page_number=217, book=6)

fr_text = """
Rapidement, vous vous frayez un chemin à travers les pierres
cassées, mais tous vos espoirs de fuite s'évanouissent lorsque
vous apercevez le terrifiant précipice qui se trouve de l'autre côté
du mur du château. A contrecœur, vous vous retournez pour
affronter votre adversaire. Avec ce gouffre béant derrière vous,
vous n'avez pas d'autre solution que d'attendre le monstre de
pied ferme et de le combattre à nouveau. Il surgit devant vous en
poussant des grognements féroces, prêt à vous mettre en pièces.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez faire un bond de côté pour tenter d'esquiver l'attaque du Yamsark, rendez-vous au :"))
    st.page_link("tomes/tome6/page_190.py", label="190", icon="📄")

    st.write_stream(stream_text("Si vous préférez rester sur place pour frapper le monstre au moment où il vous attaquera, rendez-vous au :"))
    st.page_link("tomes/tome6/page_311.py", label="311", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
