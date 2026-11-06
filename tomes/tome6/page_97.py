import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=97, book=6)

fr_text = """
L'embuscade est si soudaine que seule une chance extraordinaire
pourrait désormais vous sauver.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    roll = hazard_roll()
    if roll is not None:
        if roll <= 3:
            st.write_stream(stream_text("Si le nombre que vous avez tiré est compris entre 0 et 3, rendez-vous au :"))
            st.page_link("tomes/tome6/page_174.py", label="174", icon="📄")
        elif roll <= 6:
            st.write_stream(stream_text("Si ce même nombre est compris entre 4 et 6, rendez-vous au :"))
            st.page_link("tomes/tome6/page_313.py", label="313", icon="📄")
        else:
            st.write_stream(stream_text("S'il est compris entre 7 et 9, rendez-vous au :"))
            st.page_link("tomes/tome6/page_57.py", label="57", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
