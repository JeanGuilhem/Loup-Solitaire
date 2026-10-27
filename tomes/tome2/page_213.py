import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import stream_text, called_cookies, ls_death

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=213, book=2)

fr_text = """
Vous grimpez au sommet d'une meule de foin et vous vous
emmitouflez dans votre cape de Seigneur Kaï pour vous protéger du
vent frisquet. Vous vous endormez alors sans vous douter le moins du
monde que vous ne vous réveillerez plus jamais. En effet, l'un de vos
compagnons de voyage est un agent des Maîtres des Ténèbres et, dans
la fraîcheur de la nuit, il vient silencieusement vous assassiner sans
même que vous vous en rendiez compte. Votre quête s'achève donc ici
en même temps que votre vie.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    show_illustrations()
    ls_death()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
