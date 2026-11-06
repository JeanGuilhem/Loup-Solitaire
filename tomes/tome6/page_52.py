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

check_inventory(current_page_number=52, book=6)

fr_text = """
Une pluie de flèches s'abat sur vous. Une douleur fulgurante
explose dans votre poitrine, votre nuque et vos épaules. Vous
êtes mortellement blessé et, malgré votre ténacité à vous
raccrocher au peu de vie qui vous reste, la bataille est perdue
d'avance. Affaibli par la violence du choc et par tout le sang
que vous avez perdu, vous tombez de votre selle et vous exhalez
votre dernier souffle sur la grand-route de Varetta. Cela marque
la triste fin de votre aventure.
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
