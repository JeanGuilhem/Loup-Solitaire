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

check_inventory(current_page_number=206, book=6)

fr_text = """
Vous sentez qu'un danger vous attend dans le taillis et que les
incantations font partie du rituel d'une cérémonie sacrificatoire.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez observer la cérémonie, rendez-vous au :"))
    st.page_link("tomes/tome6/page_13.py", label="13", icon="📄")

    st.write_stream(stream_text("Si vous préférez continuer votre chemin vers Soren sans vous arrêter, rendez-vous au :"))
    st.page_link("tomes/tome6/page_102.py", label="102", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
