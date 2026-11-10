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

check_inventory(current_page_number=273, book=7)

fr_text = """
Un flot de gardes en armures se rue dans l'escalier suivi par deux
hideuses créatures à la peau noire et au visage canin qui agitent
des massues brillantes. Vous vous arc-boutez pour résister à leur
assaut, mais les gardes s'arrêtent en bas des marches et laissent
passer les deux créatures. Ces dernières avancent en poussant
d'affreux hennissements et entrechoquent l'extrémité de leurs
massues avant de les pointer d'un même mouvement dans votre
direction. Votre corps est parcouru par une douleur fulgurante
tandis qu'une flamme brûlante explose dans votre poitrine. Vous
vacillez en arrière, le corps pratiquement plié en deux par l'éclair
d'énergie destructrice, puis vous tombez au sol, victime des
massues magiques des Dhax. Votre vie et votre aventure
s'achèvent ici.
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
