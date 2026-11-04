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

check_inventory(current_page_number=390, book=5)

fr_text = """
Vous vous précipitez sur la silhouette chancelante du Seigneur
des Ténèbres Haakon, prêt à lui donner le coup de grâce. Mais au
moment où vous abaissez votre arme, son poing clouté vous
frappe au bras. Du sang jaillit de votre poignet, vos doigts
deviennent tout engourdis et vous lâchez votre arme. Haakon
attaque à nouveau, vous portant à la poitrine un violent coup qui
vous envoie valser en arrière à travers la pièce. Vous essayez de
vous redresser, mais en vain, car la bataille est terminée. Haakon
a retrouvé sa pierre étincelante ! La dernière chose que vous
voyez avant d'être consumé par la brûlante flamme bleue est le
rictus triomphant du Seigneur des Ténèbres. Votre vie et tous les
espoirs du Sommerlund prennent fin ici.
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
