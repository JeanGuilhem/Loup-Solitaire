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

check_inventory(current_page_number=240, book=7)

fr_text = """
Vous parcourez cinquante mètres avant que le passage ne
débouche sur une grande pièce circulaire. Vous apercevez,
reposant sur un socle qui se dresse en son centre, une main
humaine à la peau boursouflée et craquelée, dont les doigts noirs
sont à moitié décomposés. Derrière le socle, le passage se
poursuit tout droit, flanqué à son entrée de deux piliers en pierre
verte.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez examiner la main, rendez-vous au :"))
    st.page_link("tomes/tome7/page_226.py", label="226", icon="📄")

    st.write_stream(stream_text("Si vous préférez contourner le socle et pénétrer dans le passage, rendez-vous au :"))
    st.page_link("tomes/tome7/page_302.py", label="302", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
