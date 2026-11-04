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

check_inventory(current_page_number=45, book=5)

fr_text = """
Vous concentrez toute votre Puissance Psychique sur la main du
Garde. Celui-ci pousse un hurlement tout en desserrant les
doigts. Son poignard tombe à terre et le voilà désarmé. Qu'allez-vous faire ?
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous voulez éliminer le Garde, rendez-vous au :'))
    st.page_link("tomes/tome5/page_78.py", label="78", icon="📄")
    st.write_stream(stream_text('Si vous préférez le maîtriser et le capturer vivant, rendez-vous au :'))
    st.page_link("tomes/tome5/page_199.py", label="199", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
