import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=313, book=6)

fr_text = """
La flèche s'enfonce profondément dans votre épaule, et une
fulgurante douleur déchire tout votre corps (vous perdez 8
points d'ENDURANCE). L'impact est tel que vous basculez sur le
côté de votre selle.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-8)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-8)

    st.write_stream(stream_text('Si vous êtes toujours en vie après cette grave blessure, rendez-vous au :'))
    st.page_link("tomes/tome6/page_234.py", label="234", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
