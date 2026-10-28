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

check_inventory(current_page_number=163, book=3)

fr_text = """
Lorsque vous abaissez le levier, une porte de pierre coulisse
latéralement et ferme ainsi la pièce encombrée de débris.
Lorsque vous soulevez le levier, la porte de pierre s'ouvre à
nouveau.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez entrer dans cette pièce pour examiner ce qu'elle contient, rendez-vous au :"))
    st.page_link("tomes/tome3/page_38.py", label="38", icon="📄")
    st.write_stream(stream_text("Si vous préférez poursuivre votre chemin le long du passage orienté à l'est, rendez-vous au :"))
    st.page_link("tomes/tome3/page_237.py", label="237", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
