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

check_inventory(current_page_number=329, book=4)

fr_text = """
L'eau de la rivière vous emplit les oreilles, les yeux, le nez. Dans
votre quête désespérée d'une bouffée d'oxygène, vous êtes pris
d'une quinte de toux incontrôlable. Aveuglé, vous ne voyez pas
l'énorme rocher qui se dresse devant vous. Avec un craquement
sinistre, votre crâne vient se fracasser contre la surface de pierre
et vous sombrez à jamais dans les eaux torrentielles. Votre
mission s'achève ici en même temps que votre vie.
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
