import streamlit as st
from combat import combat
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

check_inventory(current_page_number=91, book=5)

fr_text = """
Le Garde lance violemment son marteau de guerre vers votre
visage mais vous esquivez promptement son coup en roulant sur
le côté. Sous la violence du choc les pointes acérées de l'arme
font jaillir des étincelles du mur et vous devez vous préparer à
affronter votre adversaire.
Durant tout le combat, déduisez 4 points de votre total
d'HABILETÉ puisque vous êtes désarmé.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("GARDE DU PALAIS", 14, 21)], unarmed_rounds=4, max_rounds=4)
    if outcome == "win":
        st.write_stream(stream_text("Si vous sortez vainqueur de l'affrontement en 4 Assauts ou moins, rendez-vous au :"))
        st.page_link("tomes/tome5/page_65.py", label="65", icon="📄")
    elif outcome == "rounds_over":
        st.write_stream(stream_text("Si le combat dure plus de 4 Assauts, rendez-vous au :"))
        st.page_link("tomes/tome5/page_180.py", label="180", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
