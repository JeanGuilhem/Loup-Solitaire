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

check_inventory(current_page_number=269, book=5)

fr_text = """
Vous fixez le verrou dans l'intention de le faire bouger ; derrière
vous, un bruit de pas pressés vous fait parcourir un frisson dans
le dos car vous réalisez que les Drakkars sont en train de se ruer
dans l'escalier. C'est alors que le verrou commence à bouger
lentement. Dès qu'il se trouve suffisamment tiré, vous ouvrez le
portail de pierre et vous vous élancez, inconscient des dangers
qui vous attendent derrière.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome5/page_352.py", label="352", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
