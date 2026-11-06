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

check_inventory(current_page_number=105, book=6)

fr_text = """
Quelques centaines de mètres plus loin, la rue aboutit à la
grande porte est, par laquelle vous êtes entré dans la ville.
Deux autres rues partent du corps de garde : l'une vers le nord,
l'autre vers le sud.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez vous diriger vers le nord, rendez-vous au :"))
    st.page_link("tomes/tome6/page_79.py", label="79", icon="📄")

    st.write_stream(stream_text("Si vous préférez aller vers le sud, rendez-vous au :"))
    st.page_link("tomes/tome6/page_147.py", label="147", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
