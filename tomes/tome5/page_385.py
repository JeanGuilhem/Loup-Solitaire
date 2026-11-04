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

check_inventory(current_page_number=385, book=5)

fr_text = """
La chaleur que dégage l'éclair de flamme bleue vous brûle aux
bras et au visage. Vous êtes projeté à travers la plate-forme par
l'explosion et votre corps est criblé d'éclats de cristal noir. Vous
perdez 12 points d'ENDURANCE.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-12)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-12)
    st.write_stream(stream_text("Si vous êtes toujours en vie, rendez-vous au :"))
    st.page_link("tomes/tome5/page_316.py", label="316", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
