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

check_inventory(current_page_number=349, book=7)

fr_text = """
A peine avez-vous pénétré dans le couloir que l'arche de rubis
devient complètement opaque. Vous faites demi-tour pour vous
diriger vers la pièce, mais l'entrée en est maintenant obstruée par
une barrière d'un blanc laiteux que vous ne parvenez pas à
franchir. Le crâne apparaît à nouveau mais, cette fois, son
message vous glace d'effroi :

*Le chemin que vous avez choisi mène au cœur même du
labyrinthe et vous êtes condamné à y finir vos jours.*

Hélas ! cette sinistre prophétie est exacte : vous vous êtes
aventuré trop profondément dans le labyrinthe de Zahda et ses
issues sont maintenant fermées à jamais. Vous avez cependant
survécu pendant trois semaines dans le dédale et cette prouesse
vous vaut le respect du seigneur Zahda. Malheureusement, cela
ne l'a pas convaincu de vous laisser la vie sauve... Ainsi prend fin
votre aventure.
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
