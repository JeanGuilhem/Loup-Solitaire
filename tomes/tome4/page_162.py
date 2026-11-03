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

check_inventory(current_page_number=162, book=4)

fr_text = """
Deux tunnels mènent hors de la salle, l'un est orienté à l'ouest,
l'autre au sud.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez aller à l'ouest, rendez-vous au :"))
    st.page_link("tomes/tome4/page_214.py", label="214", icon="📄")

    st.write_stream(stream_text('Si vous préférez vous diriger vers le sud, rendez-vous au :'))
    st.page_link("tomes/tome4/page_117.py", label="117", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
