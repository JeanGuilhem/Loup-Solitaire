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

check_inventory(current_page_number=312, book=3)

fr_text = """
Vous essayez désespérément de dégager votre pied, mais le
traîneau bascule déjà dans la crevasse. Vous êtes alors précipité
dans le vide. Votre chute vous semble interminable et, tandis que
vous tombez ainsi d'une hauteur de plusieurs centaines de
mètres, les cris horrifiés de vos guides retentissent à la surface,
de plus en plus lointains. Votre mission s'achève ici en même
temps que votre vie.
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
