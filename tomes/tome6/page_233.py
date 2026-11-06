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

check_inventory(current_page_number=233, book=6)

fr_text = """
Vous reconnaissez aussitôt le vieil homme qui se tient devant
vous. Il est calme à présent et il sourit. C'est le vieillard que vous
avez rencontré il y a quelques années, dans une hutte, sur la
route de Ruanon. Celui-là même qui vous donna un parchemin
qui vous mettait en garde contre les dangers du Gouffre Maudit.
« Bienvenue, Loup Solitaire. Une fois encore, nos chemins se
croisent. Les astres en ont donc décidé ainsi. »
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_6.py", label="6", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
