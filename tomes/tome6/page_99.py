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

check_inventory(current_page_number=99, book=6)

fr_text = """
Vous recevez un violent coup et, dans la seconde qui suit, vous
sentez la chaleur humide du sang qui macule votre tunique. Vous
tentez de reprendre votre souffle, mais vos forces vous
abandonnent peu à peu. Vous glissez, tombez à terre et restez
étendu, impuissant, perdant tout votre sang, sans même remarquer
l'épée brandie au-dessus de vous qui va vous porter le coup de
grâce. Votre aventure se termine prématurément ici ainsi que
votre vie.
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
