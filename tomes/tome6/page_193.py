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

check_inventory(current_page_number=193, book=6)

fr_text = """
Au moment où vous achevez le dangereux chien de garde, le
Kloon éclate en sanglots. Il sort rapidement de la pièce en
essuyant les grosses larmes écarlates qui coulent de ses yeux
cramoisis. Vous vous nettoyez les mains et quittez rapidement les
lieux.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_16.py", label="16", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
