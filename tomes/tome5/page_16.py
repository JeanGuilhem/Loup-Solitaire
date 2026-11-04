import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    pickup_button,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=16, book=5)

fr_text = """
Vous vous précipitez à l'intérieur de la cave et vous en verrouillez
la porte. En appuyant l'oreille contre le bois noueux, vous
écoutez attentivement les rumeurs de mécontentement des
soldats de Maouk. Ceux-ci ont pénétré dans le bâtiment et ils ne
seront pas longs à découvrir la porte de la cave. Vous parcourez
la pièce des yeux : elle est vide, exception faite d'un rouleau de
corde et d'un briquet. Soudain, vous remarquez qu'il existe un
autre accès donnant sur la pièce : une grille de fer en plein centre
du sol. Cependant, l'épouvantable puanteur qui s'en dégage vous
soulève le cœur.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # le livre ne dit pas de les prendre, mais rien ne l'interdit (le Briquet sert au §31)
    pickup_button("CORDE", key="corde", label="Prendre la Corde")
    pickup_button("BRIQUET À AMADOU", key="briquet", label="Prendre le Briquet")

    st.write_stream(stream_text('Si vous désirez quitter la cave en passant par cette grille, rendez-vous au :'))
    st.page_link("tomes/tome5/page_51.py", label="51", icon="📄")
    st.write_stream(stream_text('Si vous préférez rester sur place en vous préparant à combattre vos poursuivants, rendez-vous au :'))
    st.page_link("tomes/tome5/page_123.py", label="123", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
