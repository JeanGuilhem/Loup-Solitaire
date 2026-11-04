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

check_inventory(current_page_number=257, book=5)

fr_text = """
La créature vous lacère de ses griffes acérées puis vous plante son
bec dans le dos. Vous vous sentez soulevé en l'air avant d'être
projeté contre le mur par l'oiseau géant. Votre crâne se fracasse
contre le marbre et la mort est instantanée, vous épargnant
d'horribles souffrances. Votre vie et les espoirs du Sommerlund
prennent fin ici.
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
