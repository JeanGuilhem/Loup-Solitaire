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

check_inventory(current_page_number=143, book=4)

fr_text = """
Quels que soient vos efforts, l'étai refuse de bouger. Soudain, vos
poursuivants émergent des tunnels obscurs et vous attaquent. Ils
ne sont que deux, mais d'autres les suivent un peu plus loin. Le
combat est inévitable, et vous allez devoir les affronter un par un.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("1er GARDE DES TUNNELS", 16, 22)], key="garde_1")
    if outcome == "win":
        outcome_2 = combat([("2e GARDE DES TUNNELS", 15, 21)], key="garde_2", flee_after=0)
        if outcome_2 == "fled":
            st.write_stream(stream_text('Si vous parvenez à tuer le premier Garde, vous aurez le droit de prendre la fuite en vous rendant au :'))
            st.page_link("tomes/tome4/page_87.py", label="87", icon="📄")
        elif outcome_2 == "win":
            st.write_stream(stream_text('Si vous tuez les deux Gardes, rendez-vous au :'))
            st.page_link("tomes/tome4/page_230.py", label="230", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
