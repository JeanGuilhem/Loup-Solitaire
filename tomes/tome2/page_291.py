import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=291, book=2)

fr_text = """
C'est une forêt très touffue où s'enchevêtrent parmi les arbres de hautes
herbes et des buissons d'épines. Vous longez la lisière du bois pour
essayer de découvrir un sentier, mais sans succès ; il vous sera
impossible de traverser cette forêt à cheval et vous allez devoir
abandonner votre monture pour continuer votre chemin à pied.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome2/page_244.py", label="244", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
