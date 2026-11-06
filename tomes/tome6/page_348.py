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

check_inventory(current_page_number=348, book=6)

fr_text = """
Vous soulevez lentement le Marteau mais, le nœud coulant n'est
malheureusement pas assez serré, et l'instrument tombe à l'eau
avec un bruit mat et coule à pic. Déçu par tant de malchance,
vous roulez votre corde et vous la rangez dans votre Sac à Dos
avant de rejoindre Cyrilus.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome6/page_338.py", label="338", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
