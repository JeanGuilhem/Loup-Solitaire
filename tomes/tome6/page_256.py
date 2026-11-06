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

check_inventory(current_page_number=256, book=6)

fr_text = """
Barbenoire vous emmène dans une taverne qui ressemble plus à une
grande salle des fêtes qu'à une brasserie. L'Auberge des Épées
Croisées est la plus grande et la plus bruyante que vous ayez
jamais vue ! Un flot continu de soldats entre et sort à travers
l'immense porte d'entrée. Vous amenez votre cheval à l'écurie,
dont les bâtiments gigantesques pourraient recevoir les chevaux
d'une armée entière ! Vous franchissez ensuite les lourdes portes
de chêne massif avec Barbenoire et vous vous dirigez vers le bar.
« De la bière pour mon ami ! » demande Barbenoire et, aussitôt,
une serveuse se précipite pour vous servir. « Vous voyez cet homme
là-bas, dit-il en montrant du doigt une table à l'autre bout du
hall, c'est le Capitaine, venez, je vais vous présenter. »
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_211.py", label="211", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
