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

check_inventory(current_page_number=98, book=3)

fr_text = """
Vous sentez que quelqu'un, homme ou animal, se cache derrière
cette fissure, sans pouvoir deviner si l'être en question est animé
d'intentions bienveillantes ou au contraire agressives.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez examiner la fissure de plus près, rendez-vous au :'))
    st.page_link("tomes/tome3/page_49.py", label="49", icon="📄")

    st.write_stream(stream_text('Si vous préférez retourner sous votre tente, rendez-vous au :'))
    st.page_link("tomes/tome3/page_212.py", label="212", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
