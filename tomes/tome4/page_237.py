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

check_inventory(current_page_number=237, book=4)

fr_text = """
Les cadavres de vos ennemis sont allongés pêle-mêle à vos pieds.
Vous courez alors vers les portes de pierre ouvertes, soucieux de
quitter les lieux avant que le massacre soit découvert. Au-delà
des portes, une rampe descend en pente douce en direction d'un
tunnel qui s'ouvre dans le mur ouest.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome4/page_348.py", label="348", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
