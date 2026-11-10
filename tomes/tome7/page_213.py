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

check_inventory(current_page_number=213, book=7)

fr_text = """
Vous entendez un déclic, et la porte s'ouvre en glissant.
L'intérieur du sarcophage est mal éclairé, mais vous apercevez
des marches qui descendent jusqu'à une grosse porte en bois
renforcée par des clous et des barres de fer.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez entrer dans le sarcophage, rendez-vous au :"))
    st.page_link("tomes/tome7/page_37.py", label="37", icon="📄")

    st.write_stream(stream_text("Si vous préférez ne pas y entrer, rendez-vous au :"))
    st.page_link("tomes/tome7/page_102.py", label="102", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
