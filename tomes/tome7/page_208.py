import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=208, book=7)

fr_text = """
Le tronc tombe dans le vide, suivi par un déluge de pierres et de
gravats. Lorsque toute la poussière est retombée, vous êtes
toujours en train de fixer d'un air découragé l'escalier au-dessus
de vous.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous possédez une corde, rendez-vous au :"))
    st.page_link("tomes/tome7/page_310.py", label="310", icon="📄", disabled=not (has_item("CORDE")))
    st.write_stream(stream_text("Sinon, rendez-vous au :"))
    st.page_link("tomes/tome7/page_211.py", label="211", icon="📄", disabled=has_item("CORDE"))

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
