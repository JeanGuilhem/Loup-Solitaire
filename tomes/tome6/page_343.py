import streamlit as st
from combat import combat
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

check_inventory(current_page_number=343, book=6)

fr_text = """
**YAMSARK** — HABILETÉ : 22 — ENDURANCE : 38
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("YAMSARK", 22, 38)], flee_after=3)
    if outcome == "fled":
        st.write_stream(stream_text('Si vous êtes toujours en vie après 3 Assauts, vous pouvez fuir en retournant au passage voûté par lequel vous êtes entré. Rendez-vous au :'))
        st.page_link("tomes/tome6/page_305.py", label="305", icon="📄")
    elif outcome == "win":
        st.write_stream(stream_text('Si vous sortez vainqueur du combat, rendez-vous au :'))
        st.page_link("tomes/tome6/page_112.py", label="112", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
