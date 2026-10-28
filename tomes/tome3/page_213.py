import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=213, book=3)

fr_text = """
Vous dirigez la pointe du Glaive de Sommer vers la baguette de
cristal de Vonotar et, un instant plus tard, le cône de givre,
détourné de sa trajectoire, vient se fracasser contre la lame d'or.
Le Glaive de Sommer vous a une fois encore protégé de la magie
destructive de Vonotar et vous entendez le sorcier pousser un
juron rageur.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome3/page_252.py", label="252", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
