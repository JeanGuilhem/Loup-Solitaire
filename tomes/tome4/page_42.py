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

check_inventory(current_page_number=42, book=4)

fr_text = """
Vos genoux se fracassent contre la paroi et vous tombez comme
une pierre dans l'obscurité du puits ; mais bientôt la douleur
provoquée par le choc disparaît : vous venez de perdre
connaissance. Quelques dizaines de mètres plus bas, vous
tombez dans l'eau d'une rivière souterraine et, incapable de
refaire surface, vous mourez noyé en quelques instants. Votre
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
