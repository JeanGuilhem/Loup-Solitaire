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

check_inventory(current_page_number=108, book=5)

fr_text = """
Quelques mètres plus loin dans le tunnel, d'autres canalisations
déversent leurs eaux verdâtres en cascades vers le collecteur
principal. Les vapeurs qui s'en dégagent sont âcres, suffocantes,
et vous irritent les poumons et la gorge. Vous parvenez
néanmoins à franchir les cascades mais les gaz corrosifs vous
font perdre 2 points d'ENDURANCE.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-2)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-2)

    st.write_stream(stream_text("Rendez-vous ensuite au :"))
    st.page_link("tomes/tome5/page_112.py", label="112", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
