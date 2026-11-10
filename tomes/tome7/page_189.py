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

check_inventory(current_page_number=189, book=7)

fr_text = """
Vous vous baissez pour éviter le tir de votre ennemi mais, à une
distance si courte, il lui est difficile de vous manquer. Le carreau
vous atteint au moment où vous plongez en avant et il vous
transperce le crâne, vous tuant instantanément. Votre vie et
votre enquête s'achèvent ici.
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
