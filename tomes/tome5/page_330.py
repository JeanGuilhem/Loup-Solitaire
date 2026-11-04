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

check_inventory(current_page_number=330, book=5)

fr_text = """
Vous réussissez à parer le coup et à repousser le guerrier
Drakkar, mais ce dernier se reprend vite ; il vous fait face à
nouveau et vous maudit en levant son épée :
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("GUERRIER DRAKKAR", 18, 23)], max_rounds=2)
    if outcome == "win":
        st.write_stream(stream_text('Si vous gagnez le combat en 2 Assauts, ou moins, rendez-vous au :'))
        st.page_link("tomes/tome5/page_243.py", label="243", icon="📄")
    elif outcome == "rounds_over":
        st.write_stream(stream_text('Si le combat dure plus de 2 Assauts, rendez-vous au :'))
        st.page_link("tomes/tome5/page_394.py", label="394", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
