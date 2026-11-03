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

check_inventory(current_page_number=39, book=4)

fr_text = """
La flèche décrit une courbe dans le ciel envahi de fumée et
transperce le plastron étincelant de l'officier. Vous entendez son
cri de douleur dominer le vacarme de la bataille et vous voyez ses
yeux cruels se brouiller puis se fermer. Il s'effondre et glisse de sa
selle, votre flèche profondément enfoncée dans le cœur.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome4/page_148.py", label="148", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
