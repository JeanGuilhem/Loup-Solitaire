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

check_inventory(current_page_number=143, book=6)

fr_text = """
Vous avez à peine parcouru un kilomètre et demi que le pavement
de la grand-route fait place à de la terre battue. Il n'y a pas
de traces fraîches, et vous en concluez aussitôt que les
cavaliers n'ont pas pu quitter le village par cette route.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez rebrousser chemin jusqu'au village, rendez-vous au :"))
    st.page_link("tomes/tome6/page_52.py", label="52", icon="📄")

    st.write_stream(stream_text("Si vous préférez vous embusquer derrière les arbres qui bordent la route, rendez-vous au :"))
    st.page_link("tomes/tome6/page_196.py", label="196", icon="📄")

    st.write_stream(stream_text("Si vous jugez plus logique de retourner au croisement et de prendre le sentier de la colline, rendez-vous au :"))
    st.page_link("tomes/tome6/page_241.py", label="241", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
