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

check_inventory(current_page_number=265, book=4)

fr_text = """
Vous n'avez pas le temps de fouiller les cadavres, d'autres
patrouilles ont en effet été alertées par le fracas de la bataille et
sont à présent en train de se frayer un chemin parmi les arbres
pour essayer de vous rejoindre. Ecartant le feuillage taché de
sang, vous vous élancez en direction de Ruanon.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome4/page_307.py", label="307", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
