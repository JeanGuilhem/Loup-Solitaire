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

check_inventory(current_page_number=99, book=4)

fr_text = """
En raison de l'obscurité, vous ne remarquez pas un grand trou
dans les planches du pont. Vous passez au travers et vous tombez
tête la première, vous fracassant le crâne après une chute de plus
de 30 mètres. Votre mission s'achève ici, en même temps que
votre vie.
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
