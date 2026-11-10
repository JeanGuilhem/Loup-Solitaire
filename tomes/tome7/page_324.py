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

check_inventory(current_page_number=324, book=7)

fr_text = """
La chaleur est insupportable. (Vous perdez 4 points
d'ENDURANCE.) Pour éviter que vos bottes ne prennent feu et
dans l'espoir d'atteindre un endroit plus frais du tunnel, vous
continuez à courir dans ce véritable four malgré la douleur.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-4)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-4)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome7/page_24.py", label="24", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
