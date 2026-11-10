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

check_inventory(current_page_number=330, book=7)

fr_text = """
Votre Discipline Magnakaï de l'Exploration vous révèle que le
passage de gauche mène à un réseau de cellules de prison, et que
celui de droite conduit à une salle de garde et une chambre de
torture.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez prendre le passage gauche, rendez-vous au :"))
    st.page_link("tomes/tome7/page_20.py", label="20", icon="📄")
    st.write_stream(stream_text("Si vous préférez prendre le passage de droite, rendez-vous au :"))
    st.page_link("tomes/tome7/page_92.py", label="92", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
