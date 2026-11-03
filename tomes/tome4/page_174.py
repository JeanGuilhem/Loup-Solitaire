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

check_inventory(current_page_number=174, book=4)

fr_text = """
D'autres Guerriers ennemis avancent parmi les débris de la
barricade en se dirigeant vers vous. Vous vous précipitez alors
vers un grand tonneau d'eau défendu par un robuste sergent du
Sommerlund. Autour du tonneau, le sol est jonché de cadavres
ennemis. « Tuez leur chef ! » ordonnez-vous en montrant du
doigt l'officier qui commande les brigands. D'un geste rapide, le
sergent tend son arc, vise et tire. La flèche décrit une courbe dans
le ciel noirci de fumée et transperce le plastron étincelant de
l'officier. Ses yeux cruels se brouillent, puis se ferment et il glisse
de sa selle, la flèche profondément enfoncée dans le cœur.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome4/page_148.py", label="148", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
