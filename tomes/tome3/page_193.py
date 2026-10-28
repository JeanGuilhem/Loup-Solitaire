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
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=193, book=3)

fr_text = """
Vous avez les jambes couvertes d'écorchures et de bleus. Par
surcroît, vous vous êtes cogné contre une stalactite et vous
saignez du nez. Vous perdez 2 points d'ENDURANCE, mais vous
pouvez vous estimer heureux : vous avez en effet échappé de peu
à une chute au fond d'une crevasse que vous aviez failli ne pas
voir dans l'obscurité.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-2)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-2)
    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome3/page_235.py", label="235", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
