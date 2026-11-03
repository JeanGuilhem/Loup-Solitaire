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

check_inventory(current_page_number=85, book=4)

fr_text = """
Vous essayez de dégainer votre arme, mais cette créature est trop
rapide pour vous. Ses crocs s'enfoncent dans votre colonne
vertébrale et bientôt vous sentez le sang se retirer de votre corps
qui reste paralysé. Vous entendez votre arme tomber sur le sol,
puis vous vous effondrez face contre terre, votre visage heurtant
la pierre dure. Vous ne ressentez cependant aucune douleur :
toute sensibilité vous a en effet quitté et, quelques instants plus
tard, vous poussez votre dernier soupir. Votre mission s'achève
ici, en même temps que votre vie.
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
