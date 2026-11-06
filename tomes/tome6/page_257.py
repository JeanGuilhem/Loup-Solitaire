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

check_inventory(current_page_number=257, book=6)

fr_text = """
La décharge d'énergie vous brûle la poitrine comme un tison
ardent. Vous vous tordez de douleur, et rapidement vous êtes
incapable de contrôler vos mouvements et vous êtes projeté en
l'air, littéralement à la pointe de la décharge. Tout à coup,
l'éclair cesse et vous vous écrasez quelque trente mètres plus
bas, sur l'autel de pierre. Votre mission et votre vie s'achèvent
ici sur l'autel sacrificatoire des Druides de Cener.
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
