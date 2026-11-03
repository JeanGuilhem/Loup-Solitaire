import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, ls_death

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=334, book=4)

fr_text = """
Lorsque vous heurtez la surface de l'eau, votre arme vous
échappe. Saisi de panique, vous sentez alors des tentacules
gluants s'enrouler autour de votre corps. Vous vous débattez
pour essayer de vous dégager, mais vous êtes bientôt étouffé.
Quelques bulles éclatant à la surface et une cape déchirée sont les
derniers signes qui trahissent votre présence au fond de cette
tombe aquatique. Votre mission s'achève ici en même temps que
votre vie.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    show_illustrations()
    ls_death()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
