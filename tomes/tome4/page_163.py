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

check_inventory(current_page_number=163, book=4)

fr_text = """
Vous faites volte-face et vous vous enfuyez en courant, mais vous
trébuchez contre une roue de chariot brisée et vous tombez à
terre. Vous entendez alors le rire sardonique du Guerrier
vassagonien qui lève son cimeterre pour vous frapper. Son rire
cependant se transforme soudain en un hurlement de douleur.
Un instant plus tard, il s'effondre sur le sol, une flèche
profondément enfoncée dans la nuque. C'est un soldat du
Sommerlund qui vient de vous sauver.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome4/page_249.py", label="249", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
