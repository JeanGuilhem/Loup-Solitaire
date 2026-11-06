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

check_inventory(current_page_number=339, book=6)

fr_text = """
Le tunnel grimpe en pente douce jusqu'à une pièce circulaire, et
le niveau de l'eau baisse au fur et à mesure que vous vous
approchez de la pièce voûtée.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    light = has_item("SPHÈRE DE FEU") or has_item("BRIQUET À AMADOU") or has_item("TORCHE")
    st.write_stream(stream_text("Si vous possédez une Sphère de Feu de Kalte, un Briquet d'Amadou ou une Torche, rendez-vous au :"))
    if light:
        st.page_link("tomes/tome6/page_80.py", label="80", icon="📄")
    else:
        st.page_link("tomes/tome6/page_80.py", label="80", icon="📄", disabled=True)

    st.write_stream(stream_text('Si vous ne possédez aucun de ces objets, rendez-vous au :'))
    if light:
        st.page_link("tomes/tome6/page_90.py", label="90", icon="📄", disabled=True)
    else:
        st.page_link("tomes/tome6/page_90.py", label="90", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
