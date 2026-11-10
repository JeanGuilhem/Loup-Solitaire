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

check_inventory(current_page_number=292, book=7)

fr_text = """
L'air se raréfie et, lentement, douloureusement, vous sentez votre
corps s'affaiblir et sombrez peu à peu dans l'inconscience, ce qui
vous épargne les terribles douleurs d'une mort par asphyxie.
Votre vie et votre quête s'achèvent ici.
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
