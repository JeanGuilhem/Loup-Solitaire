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

check_inventory(current_page_number=57, book=6)

fr_text = """
La décharge vous frappe avec une telle violence que vous êtes
désarçonné et jeté brutalement à terre. Vous restez quelques
instants étourdi par le choc. Comme vous essayez péniblement de
reprendre votre souffle, une paralysie terrifiante envahit
rapidement votre poitrine puis s'étend progressivement à vos
membres. Vous ne ressentez aucune douleur, simplement un
engourdissement glacial qui annihile toute résistance de votre
part pour lutter contre la mort. Votre aventure et votre vie
s'achèvent ici à la Porte de Denka.
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
