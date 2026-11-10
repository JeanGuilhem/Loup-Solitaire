import streamlit as st
from inventory import (
    check_inventory,
    choose_item_to_lose,
    display_inventory,
    end_page,
    has_item,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=32, book=7)

fr_text = """
Au moment où vous parvenez à abaisser le levier de la pointe de
votre arme, vous sentez de l'eau vous mouiller le bras : le courant
s'est inversé, et la statue aspire désormais l'eau à une vitesse
étourdissante ! Votre arme vous échappe de la main (n'oubliez
pas de la rayer de votre Feuille d'Aventure), mais vous parvenez,
heureusement, à retirer votre bras et à nager vers la surface. En
l'espace de quelques minutes, le niveau de l'eau s'est abaissé
jusqu'à la bouche de la statue, où il se maintient. Soudain, la
porte craque et éclate sous la pression de l'énorme masse d'eau
qu'elle contenait.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # l'arme qui a servi à abaisser le levier est perdue : le joueur la choisit
    weapons = list(st.session_state.weapons) + (["GLAIVE DE SOMMER"] if has_item("GLAIVE DE SOMMER") else [])
    settled = choose_item_to_lose(weapons, key="arme_32", label="Quelle arme avez-vous utilisée (et perdue) ?")
    if settled:
        st.write_stream(stream_text('Rendez-vous au :'))
        st.page_link("tomes/tome7/page_172.py", label="172", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
