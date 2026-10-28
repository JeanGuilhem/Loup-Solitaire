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

check_inventory(current_page_number=75, book=3)

fr_text = """
Ces traces ont été laissées par de redoutables créatures
carnivores que l'on appelle des Bakanals. Si vous veniez à les
rencontrer dans l'espace étroit et sombre d'un tunnel, vos
chances de survie seraient fort minces en vérité. Bien que votre
Discipline Kaï vous ait permis d'identifier ces traces, il vous est
impossible cependant de deviner dans quel tunnel les Bakanals
se trouvent à présent.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez emprunter le tunnel de gauche, rendez-vous au :'))
    st.page_link("tomes/tome3/page_235.py", label="235", icon="📄")

    st.write_stream(stream_text('Si vous préférez le tunnel de droite, rendez-vous au :'))
    st.page_link("tomes/tome3/page_114.py", label="114", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
