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

check_inventory(current_page_number=17, book=4)

fr_text = """
La pointe d'une lance vous a écorché l'avant-bras. Il ne s'agit que
d'une simple égratignure et pourtant votre bras s'est soudain
engourdi au point que vous ne pouvez plus le remuer. Vous
frappez votre agresseur, mais votre coup est trop faible et mal
porté pour se révéler efficace. Votre vue se trouble, vous ne
parvenez plus à coordonner vos mouvements. Une terreur
aveugle vous envahit lorsque vous vous rendez compte soudain
que ces bandits utilisent des armes empoisonnées. Une autre
lance vous atteint à nouveau au bras et une autre encore
s'enfonce dans votre poitrine. Vous sombrez peu à peu dans
l'obscurité en emportant de ce monde une dernière vision: celle
du rictus triomphant de vos assassins en train de vous achever.
Votre mission se termine ici en même temps que votre vie.
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
