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

check_inventory(current_page_number=177, book=4)

fr_text = """
Vous n'avez fait qu'un pas à l'intérieur de la caverne, lorsqu'un
coup porté par-derrière vous assomme net. Deux Gardes vous
avaient vu au croisement et vous ont tendu cette embuscade.
Votre équipement est confisqué et vous êtes jeté sans
connaissance dans une cellule par les hommes de Barraka. Il
vous sera désormais impossible d'empêcher le sacrifice et,
lorsque la porte de votre prison s'ouvrira à nouveau, c'est la main
décharnée d'un squelette qui aura tourné la clé dans la serrure.
Votre mission s'achève ici.
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
