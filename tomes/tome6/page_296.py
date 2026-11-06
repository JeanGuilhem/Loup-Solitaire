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

check_inventory(current_page_number=296, book=6)

fr_text = """
Vous avez bien atteint votre cible, mais la flèche ne pénètre pas
dans l'épaisse cuirasse de métal noir qui protège le dos du
guerrier. Vous regardez, déçu, votre flèche ricocher avant de
disparaître derrière le parapet du pont. Sans plus attendre, vous
remettez votre arc en bandoulière et vous montez sur votre cheval,
puis vous vous lancez à la poursuite des ravisseurs avant qu'ils
ne disparaissent de votre vue.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_39.py", label="39", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
