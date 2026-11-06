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

check_inventory(current_page_number=64, book=6)

fr_text = """
Vous rebroussez chemin jusqu'au croisement et vous vous accordez
une pause afin de choisir le meilleur trajet.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez aller tout droit, rendez-vous au :"))
    st.page_link("tomes/tome6/page_339.py", label="339", icon="📄")

    st.write_stream(stream_text("Si vous préférez prendre le tunnel de gauche, rendez-vous au :"))
    st.page_link("tomes/tome6/page_269.py", label="269", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
