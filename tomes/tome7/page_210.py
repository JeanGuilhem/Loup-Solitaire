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

check_inventory(current_page_number=210, book=7)

fr_text = """
Une fois encore, vous faites appel à votre Maîtrise Kaï pour vous
défendre contre les menaces des reptiles, et votre discipline est
toujours aussi efficace. Les serpents font demi-tour et rampent
vers leur nid pour se mettre à l'abri, aussi effrayés en vous voyant
que vous l'avez été vous-même en les apercevant.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome7/page_346.py", label="346", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
