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

check_inventory(current_page_number=163, book=7)

fr_text = """
Vous passez sous l'arche de jade et, immédiatement, une vague
de chaleur insupportable vous envahit des pieds à la tête. La
chaleur monte en vous, provoquant une douleur intolérable.
Vous venez de franchir une porte d'anéantissement. Avant de
passer de vie à trépas, vous entendez le rire sardonique de Zahda,
qui assiste depuis le début au spectacle de votre mort,
tranquillement installé sur une plate-forme surélevée, au milieu
des brumes du plafond. Votre vie et votre aventure se terminent,
hélas ! ici.
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
