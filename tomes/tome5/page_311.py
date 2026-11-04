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

check_inventory(current_page_number=311, book=5)

fr_text = """
Vous levez votre Glaive d'or juste à temps pour parer la décharge
d'énergie brute. Celle-ci crisse sur votre lame et va exploser
contre le mur de la pièce, creusant dans le roc un trou de
plusieurs dizaines de centimètres de profondeur tout en
dégageant un épais nuage de poussière. Sous le choc, le Glaive de
Sommer vous échappe des mains et fend l'air en décrivant un arc
de cercle avant d'aller se planter avec force dans le sol. Roulant
sur vous-même, vous vous abritez derrière une colonne tandis
que Haakon vous crie ironiquement : « Ta dernière heure est
arrivée, Seigneur Kaï ! »
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous désirez aller rechercher le Glaive de Sommer, rendez-vous au :'))
    st.page_link("tomes/tome5/page_278.py", label="278", icon="📄")

    st.write_stream(stream_text('Si vous préférez tenter de gagner un autre abri avant que la poussière ne soit retombée, rendez-vous au :'))
    st.page_link("tomes/tome5/page_350.py", label="350", icon="📄")

    st.write_stream(stream_text('Si vous jugez préférable de rester là où vous êtes, rendez-vous au :'))
    st.page_link("tomes/tome5/page_230.py", label="230", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
