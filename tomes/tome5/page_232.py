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

check_inventory(current_page_number=232, book=5)

fr_text = """
Vous essayez de vous écarter de la trajectoire de la lame mortelle
mais, dans l'obscurité, vous ne pouvez pas voir distinctement la
direction qu'elle a prise. Le coup vous atteint à la poitrine et sa
violence chasse l'air de vos poumons. Vous voyez trente-six
chandelles, puis une explosion vous brise les tympans. Vous
tombez à genoux et une sensation d'engourdissement se répand
dans votre corps. A travers les brumes tourbillonnantes, vous
voyez le Drakkar basculer en arrière, la cuirasse déchirée par la
balle qu'un Nain vient de tirer. Banedon apparaît, le visage
décomposé, couleur de cendres. Ses lèvres remuent, mais vous
ne pouvez pas comprendre les paroles qu'elles prononcent. Des
images du Sommerlund flottent devant vos yeux, puis disparais-sent peu à peu tandis que vous sombrez dans l'inconscience.
Votre vie et les derniers espoirs pour le Sommerlund prennent
fin ici.
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
