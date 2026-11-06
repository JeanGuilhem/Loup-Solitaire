import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_flag,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

# Fait testé : "tournoi de tir à l'arc gagné" (posé au paragraphe 252).

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=325, book=6)

fr_text = """
Vous n'avez pas besoin de chercher longtemps le propriétaire du
cheval : il arrive en ce moment même à grands pas vers vous. Il
vous reconnaît aussitôt et vous adresse un petit signe amical de
la main.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous avez remporté le tournoi de tir à l'arc, rendez-vous au :"))
    if has_flag("tournoi de tir à l'arc gagné"):
        st.page_link("tomes/tome6/page_45.py", label="45", icon="📄")
    else:
        st.page_link("tomes/tome6/page_45.py", label="45", icon="📄", disabled=True)

    st.write_stream(stream_text("Si ce n'est pas le cas, rendez-vous au :"))
    if has_flag("tournoi de tir à l'arc gagné"):
        st.page_link("tomes/tome6/page_132.py", label="132", icon="📄", disabled=True)
    else:
        st.page_link("tomes/tome6/page_132.py", label="132", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
