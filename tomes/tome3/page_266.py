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

check_inventory(current_page_number=266, book=3)

fr_text = """
Vous essayez désespérément de vous libérer le pied, mais le
traîneau bascule déjà dans le vide. Dans un dernier effort, vous
parvenez enfin à vous dégager, mais il est trop tard et vous
tombez dans la crevasse en entendant les cris horrifiés de vos guides.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome3/page_21.py", label="21", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
