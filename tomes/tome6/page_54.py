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

check_inventory(current_page_number=54, book=6)

fr_text = """
Il ne vous reste pas d'autre choix que de passer la nuit dans
l'écurie, en compagnie de votre cheval. L'endroit est à la fois
humide et nauséabond, et vous y passez des heures exécrables
qui, loin de vous procurer un repos salutaire, vous font perdre
2 points d'ENDURANCE.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-2)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-2)

    st.write_stream(stream_text("A présent, rendez-vous au :"))
    st.page_link("tomes/tome6/page_272.py", label="272", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
