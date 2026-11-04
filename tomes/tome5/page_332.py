import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=332, book=5)

fr_text = """
Quittant la tonnelle de verdure, vous vous précipitez vers le mur
d'enceinte de l'Arboretum. Vous vous frayez difficilement un
chemin à travers la végétation dense, mais vous finissez par
découvrir une étroite porte voûtée donnant sur une pièce à ciel
ouvert. De là, un escalier conduit à un chemin de ronde au bout
duquel se trouve une porte en pierre. Vous avez gravi la moitié
des marches lorsque, soudain, le bruit mat d'une arbalète que
l'on arme vous glace le sang. Vous retourner maintenant serait
un pur suicide ; aussi vous élancez-vous rapidement vers le haut
de l'escalier en serrant les dents. A ce moment, une volée de
flèches fend l'air dans votre direction.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome5/page_372.py", label="372", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
