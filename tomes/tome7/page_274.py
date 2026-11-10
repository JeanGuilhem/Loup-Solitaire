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

check_inventory(current_page_number=274, book=7)

fr_text = """
A première vue, la porte semble complètement lisse, et vous
n'apercevez ni serrure, ni barre, ni gond sur sa surface polie.
Cependant, en regardant de plus près, vous découvrez un
minuscule trou de serrure situé juste à côté de la porte.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    key = has_item("CLÉ D'OR")
    st.write_stream(stream_text("Si vous possédez une Clé d'Or, rendez-vous au :"))
    st.page_link("tomes/tome7/page_333.py", label="333", icon="📄", disabled=not key)

    st.write_stream(stream_text("Si vous ne possédez pas cet Objet Spécial, rendez-vous au :"))
    st.page_link("tomes/tome7/page_54.py", label="54", icon="📄", disabled=key)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
