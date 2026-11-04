import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    lose_everything,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=89, book=5)

fr_text = """
Une douleur aiguë vous traverse la mâchoire lorsque la fléchette
se plante dans votre chair. Un instant plus tard, tout se met à
tourner autour de vous, vos yeux se voilent et vous perdez
connaissance, échappant ainsi à la douleur. Lorsque vous vous
réveillez, vous vous retrouvez à nouveau dans la cellule infestée
de cafards dont vous vous étiez enfui. On vous a enlevé vos armes
ainsi que tout votre équipement, et il ne vous reste plus
maintenant qu'à attendre l'arrivée du Zakhan.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        lose_everything()
    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome5/page_18.py", label="18", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
