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

check_inventory(current_page_number=303, book=7)

fr_text = """
Vous suivez le chemin de pierre et vous arrivez bientôt à la
fissure. Vous entendez une espèce de sifflement dans l'obscurité
et, soudain, une forme courte et noire perce la surface du lac. Un
horrible gargouillement déchire le silence de la nuit, et la chose
vole droit vers vous. Vous vous précipitez par l'étroite fissure à
l'intérieur de la paroi rocheuse.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome7/page_16.py", label="16", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
