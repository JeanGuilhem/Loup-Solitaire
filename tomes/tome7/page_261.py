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

check_inventory(current_page_number=261, book=7)

fr_text = """
Le crâne et l'écho de sa voix disparaissent peu à peu et sont
bientôt remplacés par des bruits de pas lourds qui résonnent
dans le tunnel derrière vous. Le sombre couloir semble désert
mais les pas se rapprochent rapidement.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    drink = has_item("FLASQUE DE VIN") or has_item("BOUTEILLE DE VIN") or has_item("BOUTEILLE D'EAU")
    st.write_stream(stream_text("Si vous avez une Flasque de Vin ou une Bouteille d'Eau, rendez-vous au :"))
    st.page_link("tomes/tome7/page_18.py", label="18", icon="📄", disabled=not drink)

    st.write_stream(stream_text("Si vous ne possédez aucun de ces objets, rendez-vous au :"))
    st.page_link("tomes/tome7/page_304.py", label="304", icon="📄", disabled=drink)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
