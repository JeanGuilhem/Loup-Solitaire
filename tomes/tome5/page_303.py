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

check_inventory(current_page_number=303, book=5)

fr_text = """
Vous vous approchez furtivement de la sentinelle par-derrière et
vous la réduisez définitivement au silence en lui tordant le cou.
Vous traînez ensuite le corps un peu plus loin et vous le cachez
sous une brouette avant d'entrer dans le Tombeau.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous maintenant au :'))
    st.page_link("tomes/tome5/page_395.py", label="395", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
