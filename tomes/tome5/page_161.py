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

check_inventory(current_page_number=161, book=5)

fr_text = """
Heureusement pour vous, votre ennemi avait juste l'intention de
vous assommer et vous retrouvez la moitié des points
d'ENDURANCE que vous aviez perdus au cours de la bataille.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # la moitié des points perdus a déjà été rendue à la fin du combat (combat(..., knockout=True))
    st.metric(label="Endurance", value=st.session_state.endurance)
    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome5/page_69.py", label="69", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
