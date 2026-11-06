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

check_inventory(current_page_number=277, book=6)

fr_text = """
Mais l'homme réagit à la vitesse de l'éclair. Il vous jette le
plateau en argent à la tête puis disparaît derrière un rideau, au
fond de l'atelier.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez vous lancer à sa poursuite, rendez-vous au :"))
    st.page_link("tomes/tome6/page_94.py", label="94", icon="📄")

    st.write_stream(stream_text("Si vous préférez le laisser et quitter l'atelier d'empaillage, rendez-vous au :"))
    st.page_link("tomes/tome6/page_279.py", label="279", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
