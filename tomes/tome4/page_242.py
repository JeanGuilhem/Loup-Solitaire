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

check_inventory(current_page_number=242, book=4)

fr_text = """
Vous vous jetez de côté pour éviter le disque mortel, mais vos
réflexes n'ont pas été suffisamment rapides pour vous sauver.
L'arme tranchante comme un rasoir s'enfonce dans votre gorge
en vous projetant en arrière sous la force du choc. Votre mission
s'achève ici en même temps que votre vie.
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
