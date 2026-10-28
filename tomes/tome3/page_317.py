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

check_inventory(current_page_number=317, book=3)

fr_text = """
La porte de pierre commence à s'ouvrir en grinçant, mais elle se
coince brusquement alors qu'elle est simplement entrebâillée.
L'ouverture ainsi ménagée ne fait guère plus d'une soixantaine de
centimètres de large et vous parvenez tout juste à vous y faufiler.
Derrière la porte, vous découvrez une pièce à la température
glaciale et qui sent le renfermé. De toute évidence, il doit y avoir
une éternité que personne n'est entré ici. Des étagères de pierre
fixées au mur sont surchargées de bouteilles et de flacons, tandis
que, sur une table, au centre de la pièce, est posé un sac rempli
de potions de différentes couleurs.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez examiner ces anciennes potions, rendez-vous au :"))
    st.page_link("tomes/tome3/page_10.py", label="10", icon="📄")
    st.write_stream(stream_text("Si vous préférez quitter les lieux et poursuivre votre chemin en direction du nord, rendez-vous au :"))
    st.page_link("tomes/tome3/page_126.py", label="126", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
