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

check_inventory(current_page_number=171, book=7)

fr_text = """
Votre maîtrise Kaï vous révèle l'existence d'une porte secrète
située dans le mur, au bas des marches. Une des briques est
beaucoup plus lisse que les autres, et vous sentez qu'elle doit
actionner la serrure qui ferme la porte.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez appuyer sur la brique, rendez-vous au :"))
    st.page_link("tomes/tome7/page_14.py", label="14", icon="📄")

    st.write_stream(stream_text("Si vous préférez suivre le tunnel vers l'ouest, rendez-vous au :"))
    st.page_link("tomes/tome7/page_29.py", label="29", icon="📄")

    st.write_stream(stream_text("Si vous préférez suivre le tunnel vers l'est, rendez-vous au :"))
    st.page_link("tomes/tome7/page_272.py", label="272", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
