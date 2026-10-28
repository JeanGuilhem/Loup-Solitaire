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

check_inventory(current_page_number=255, book=3)

fr_text = """
La mise en pratique de la Discipline Kaï de l'Orientation vous
permet de savoir que le tunnel de gauche est orienté au nord
tandis que celui de droite mène vers l'est. Or, Ikaya se trouve à
environ 80 kilomètres en direction du nord.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez prendre le tunnel de gauche, rendez-vous au :'))
    st.page_link("tomes/tome3/page_125.py", label="125", icon="📄")

    st.write_stream(stream_text('Si vous préférez emprunter celui de droite, rendez-vous au :'))
    st.page_link("tomes/tome3/page_184.py", label="184", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
