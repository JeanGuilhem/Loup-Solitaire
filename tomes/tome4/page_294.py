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

check_inventory(current_page_number=294, book=4)

fr_text = """
Le chariot s'arrête sous un portique et les hommes au visage
hagard sont reconduits dans le tunnel. Il vous faut attendre une
heure avant que l'entrée du souterrain soit à nouveau libre. Vous
vous glissez alors hors du chariot, et vous courez le long de la
voie ferrée. Vous apercevez d'un côté une forêt touffue et de
l'autre une profonde excavation aux parois abruptes. Vous vous
précipitez vers l'abri des arbres en comprenant à ce moment que
l'étranger au visage ruisselant de sueur avait essayé de vous aider
à fuir. Vous lui adressez de silencieux remerciements, et vous
poursuivez votre chemin en direction de Ruanon.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome4/page_200.py", label="200", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
