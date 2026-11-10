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

check_inventory(current_page_number=222, book=7)

fr_text = """
Vous glissez et tombez, mais parvenez miraculeusement à vous
accrocher au pont invisible. Ignorant la douleur cuisante qui
vous brûle les jambes, vous concentrez tous vos efforts pour
reprendre pied sur le pont. Hélas, juste au moment où vous y
parvenez, le fouet claque à nouveau, et vous recevez un violent
coup sur le dos (vous perdez 1 autre point d'ENDURANCE). Le
fouet claque une troisième fois mais sans vous atteindre car vous
avez rampé rapidement sur le pont et vous êtes maintenant hors
de portée de ses cruelles morsures.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-1)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-1)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome7/page_6.py", label="6", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
