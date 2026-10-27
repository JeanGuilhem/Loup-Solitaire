import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=27, book=2)

fr_text = """
Vous marchez pendant plus de trois heures le long de la route déserte
qui suit la côte. Lorsque enfin la nuit tombe, vous êtes épuisé et vous
décidez de prendre quelque repos jusqu'à l'aube. Vous vous remettrez
alors en chemin. Mais bientôt, certains récits que les Maîtres Kaï vous
ont faits vous reviennent en mémoire : il y était question du Pays
Sauvage qui s'étend entre le Sommerlund et Durenor ; la nuit, des
hordes de chiens féroces parcourent ces terres désolées, en quête de
nourriture. Le souvenir de ces contes vous incite à la prudence et vous
décidez de passer la nuit à l'abri d'un grand arbre au feuillage touffu,
planté au bord du chemin. Vous prenez là un repos réparateur qui vous
rend 2 points d'ENDURANCE (si tant est que vous en ayez perdu).
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        before = st.session_state.endurance
        change_endurance(2)
        st.session_state["visibility_rest"] = st.session_state.endurance - before
    st.metric(label="Endurance", value=st.session_state.endurance, delta=st.session_state.get("visibility_rest") or 0)
    st.write_stream(stream_text("Rendez-vous ensuite au :"))
    st.page_link("tomes/tome2/page_312.py", label="312", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
