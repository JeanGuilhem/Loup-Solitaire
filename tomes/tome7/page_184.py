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

check_inventory(current_page_number=184, book=7)

fr_text = """
Vous avez l'impression que votre poitrine va exploser, mais la
porte ne s'ouvre toujours pas.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous possédez une fiole de Pilules Bleues, rendez-vous au :"))
    st.page_link("tomes/tome7/page_230.py", label="230", icon="📄", disabled=not has_item("FIOLE DE PILULES BLEUES"))

    st.write_stream(stream_text("Si vous souhaitez toujours tenter d'ouvrir la porte à l'aide de votre Discipline Magnakaï, rendez-vous au :"))
    st.page_link("tomes/tome7/page_313.py", label="313", icon="📄")

    st.write_stream(stream_text("Si vous préférez nager vers la surface, rendez-vous au :"))
    st.page_link("tomes/tome7/page_153.py", label="153", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
