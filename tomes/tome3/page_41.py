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

check_inventory(current_page_number=41, book=3)

fr_text = """
Vous ôtez le Triangle de Pierre Bleue de votre cou et vous
l'appliquez contre le mur de granite : il s'adapte parfaitement au
triangle gravé. Aussitôt, vous sentez trembler le rebord sur lequel
vous vous tenez et vous entendez le grincement de pierres qui
frottent les unes contre les autres. La porte s'ouvre mais, après
s'être entrebâillée d'un mètre environ, elle commence déjà à se
refermer. Sans hésiter un instant, vous plongez à l'intérieur de la
forteresse et la porte claque derrière vous dans un grand bruit.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome3/page_221.py", label="221", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
