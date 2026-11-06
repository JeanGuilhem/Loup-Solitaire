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

check_inventory(current_page_number=269, book=6)

fr_text = """
A une centaine de mètres devant vous, vous apercevez une volée de
marches en pierre menant à une trappe aménagée dans le plafond.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez examiner la trappe, rendez-vous au :"))
    st.page_link("tomes/tome6/page_107.py", label="107", icon="📄")

    st.write_stream(stream_text("Si vous préférez continuer le long de l'égout, rendez-vous au :"))
    st.page_link("tomes/tome6/page_120.py", label="120", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
