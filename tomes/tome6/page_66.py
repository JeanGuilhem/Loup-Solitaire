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

check_inventory(current_page_number=66, book=6)

fr_text = """
L'homme réagit promptement à votre attaque : il vous lance le
plateau d'argent à la tête et s'enfuit vers l'arrière-boutique
par une ouverture dissimulée derrière un épais rideau.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous désirez le suivre, rendez-vous au :"))
    st.page_link("tomes/tome6/page_324.py", label="324", icon="📄")

    st.write_stream(stream_text("Si vous préférez le laisser aller et sortir du magasin, rendez-vous au :"))
    st.page_link("tomes/tome6/page_279.py", label="279", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
