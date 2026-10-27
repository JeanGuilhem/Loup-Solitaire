import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=202, book=2)

fr_text = """
Le soldat vous salue et vous laisse franchir la porte rouge. Vous arrivez
alors sur une place éclairée par les lumières du port. A votre grand
soulagement, vous apercevez un drapeau familier qui flotte au vent
frais de la nuit : un soleil surmonté d'une couronne; c'est l'étendard du
Sommerlund, et ces colonnes de marbre qui se dressent devant vous
marquent l'entrée du consulat. Lorsque vous montez les marches de
pierre qui mènent à la porte du bâtiment, les gardes sommerlundois en
faction vous reconnaissent aussitôt. Ils disparaissent à l'intérieur et
reviennent peu après en compagnie d'un homme de haute taille, aux
cheveux grisonnants : c'est un fonctionnaire du consulat. L'expression
inquiète de son visage se métamorphose en un sourire épanoui lorsqu'il
aperçoit votre cape et votre tunique de Seigneur Kaï. « Dieu soit loué,
vous êtes vivant, Seigneur Kaï. Les rares nouvelles qui sont parvenues
jusqu'ici nous ont plongés dans l'angoisse. » Vous êtes immédiatement
conduit à l'intérieur du bâtiment et introduit dans le bureau occupé par
le représentant du Sommerlund, le Lieutenant Général Rhygar.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome2/page_31.py", label="31", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
