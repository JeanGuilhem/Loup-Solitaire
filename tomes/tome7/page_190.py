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

check_inventory(current_page_number=190, book=7)

fr_text = """
Vous dirigez toute la puissance de votre Discipline Psychique sur
l'immense œil blessé. Le tentacule se met à trembler et relâche
son étreinte. Vous en profitez aussitôt pour vous dégager et vous
vous relevez tant bien que mal. L'utilisation de votre Discipline
Magnakaï vous a coûté 2 points d'ENDURANCE, mais vous a
sauvé d'une mort terrifiante. Faites les modifications nécessaires
sur votre Feuille d'Aventure.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-2)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-2)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome7/page_41.py", label="41", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
