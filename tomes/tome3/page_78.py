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

check_inventory(current_page_number=78, book=3)

fr_text = """
Vous vous préparez en hâte et vous sortez de la tente. Le vent
s'est intensifié et il emporte la neige poudreuse en petits
tourbillons qui réduisent considérablement la visibilité. Une
ombre sur votre droite trahit la présence du Bakanal qui bondit
sur vous. Vous n'avez plus le temps d'éviter son Assaut, et il vous
faut le combattre jusqu'à la mort.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("BAKANAL", 19, 30)])
    if outcome == "win":

        st.write_stream(stream_text('Si vous êtes vainqueur, rendez-vous au :'))
        st.page_link("tomes/tome3/page_245.py", label="245", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
