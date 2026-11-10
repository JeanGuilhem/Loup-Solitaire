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

check_inventory(current_page_number=51, book=7)

fr_text = """
Après plusieurs tentatives, vous réussissez enfin à faire du feu. La
flamme brille d'un vif éclat pendant quelques secondes, mais elle
s'éteint subitement après avoir consumé le peu d'oxygène qui
restait à l'intérieur de la bulle. Vous prenant la gorge à deux
mains, vous tombez lentement à genoux, suffocant, dans cet
espace translucide qui sera votre tombe. Votre aventure et votre
vie se terminent ici.
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
