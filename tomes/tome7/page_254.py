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

check_inventory(current_page_number=254, book=7)

fr_text = """
Vous plongez avec précision en évitant les corps qui flottent à la
surface et vous pénétrez dans l'eau à un angle parfait.
Malheureusement, l'eau est bouillante, car des éruptions de lave
en fusion ont percé la croûte fragile du fond du lac. Vous essayez
de remonter à la surface, mais vos membres sont paralysés par la
chaleur, et vous sombrez comme une pierre peu de temps après.
Votre vie et votre mission se terminent tragiquement ici.
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
