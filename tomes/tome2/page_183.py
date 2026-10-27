import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import stream_text, called_cookies, hazard_roll

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=183, book=2)

fr_text = """
Au bord du terrain où vous avez établi votre camp, la forêt descend en
pente raide ; dans votre hâte, vous trébuchez et vous tombez tête la
première parmi les arbres.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(
        stream_text(
            "Utilisez la Table de Hasard pour obtenir un chiffre. Entre 0 et 8, rendez-vous au 311. Si "
            "le chiffre obtenu est un 9, rendez-vous au 159."
        )
    )
    number = hazard_roll()
    if number is not None and 0 <= number <= 8:
        st.page_link("tomes/tome2/page_311.py", label="311", icon="📄")
    elif number is not None and number == 9:
        st.page_link("tomes/tome2/page_159.py", label="159", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
