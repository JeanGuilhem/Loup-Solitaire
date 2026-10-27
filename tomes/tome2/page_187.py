import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    pickup_button,
    pickup_gold,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=187, book=2)

fr_text = """
En fouillant rapidement leurs cadavres, vous découvrez les objets
suivants : 2 Lances, 2 Epées, 6 Pièces d'Or. Si vous décidez d'emporter
l'un ou l'autre de ces objets, n'oubliez pas de modifier votre Feuille
d'Aventure en conséquence. Vous précipitez ensuite les corps des
soldats dans les eaux du chenal et vous vous hâtez de franchir le pont,
de peur que quelqu'un n'ait été témoin de la scène. Une fois parvenu de
l'autre côté, vous marchez pendant une heure sur un chemin forestier et
vous calez confortablement votre Sac à Dos sur vos épaules et vous
prenez la direction de l'est.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Vous pouvez emporter les objets que vous souhaitez :"))
    pickup_button("LANCE", key="lance_1", label="Prendre une Lance")
    pickup_button("LANCE", key="lance_2", label="Prendre une Lance")
    pickup_button("ÉPÉE", key="epee_1", label="Prendre une Épée")
    pickup_button("ÉPÉE", key="epee_2", label="Prendre une Épée")
    pickup_gold(6)

    st.write_stream(stream_text("Rendez-vous ensuite au :"))
    st.page_link("tomes/tome2/page_265.py", label="265", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
