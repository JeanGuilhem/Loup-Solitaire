import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=254, book=3)

fr_text = """
Vous découvrez une autre porte de pierre dans le mur ouest du
couloir. A travers un judas aménagé en son centre, vous
apercevez, de l'autre côté, une cellule. Un vieil homme est
recroquevillé dans un coin de la prison, les cheveux et le visage
souillés de sang et de crasse. Sa toge bleue est si sale qu'on ne
voit presque plus les croissants de lune et les étoiles dont l'étoffe
est brodée.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez ouvrir la porte de cette cellule, rendez-vous au :'))
    st.page_link("tomes/tome3/page_56.py", label="56", icon="📄")

    st.write_stream(stream_text('Si vous préférez ne pas prêter attention au vieil homme et poursuivre votre chemin le long du couloir, rendez-vous au :'))
    st.page_link("tomes/tome3/page_276.py", label="276", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
