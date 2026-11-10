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

check_inventory(current_page_number=331, book=7)

fr_text = """
Votre mort est rapide. Vous êtes tout près de la gueule de la
créature mais toute la partie supérieure de votre corps est
paralysée par sa salive corrosive, ce qui vous évite une terrible
agonie : être dévoré vivant ! Votre vie et votre quête s'achèvent
ici.
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
