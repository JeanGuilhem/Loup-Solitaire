import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=45, book=3)

fr_unknown_item = "Vous ne possédez pas cet objet."

fr_text = """
Le coffre est décoré de têtes de créatures grotesques et
grimaçantes. Leur expression obscène et leur aspect monstrueux
vous font frissonner de dégoût. Au milieu du couvercle, un gros
bloc de pierre sculptée représente un visage hideux dont la
bouche est constituée par un trou de serrure.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous possédez une Clé d'Argent, rendez-vous au :"))
    if has_item("CLÉ D'ARGENT"):
        st.page_link("tomes/tome3/page_303.py", label="303", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome3/page_303.py", label="303", icon="📄", disabled=True)

    st.write_stream(stream_text('Dans le cas contraire, rendez-vous au :'))
    st.page_link("tomes/tome3/page_15.py", label="15", icon="📄", disabled=has_item("CLÉ D'ARGENT"))

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
