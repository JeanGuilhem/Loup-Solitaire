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

check_inventory(current_page_number=2, book=3)

fr_text = """
Vous découvrez à votre droite une porte de pierre habilement
dissimulée dans les sculptures contournées qui couvrent le mur.
En examinant de près ces sculptures, vous apercevez un levier.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez tirer ce levier, rendez-vous au :'))
    st.page_link("tomes/tome3/page_290.py", label="290", icon="📄")

    st.write_stream(stream_text("Sinon, vous pouvez continuer à monter l'escalier en vous rendant au :"))
    st.page_link("tomes/tome3/page_76.py", label="76", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
