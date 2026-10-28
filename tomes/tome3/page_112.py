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

check_inventory(current_page_number=112, book=3)

fr_text = """
Avant que vous ne vous installiez pour la nuit dans la tiédeur de
vos Couvertures de Fourrure, Fenor prépare un solide Repas
constitué de viande séchée marinée dans du Wanlo, un alcool
fort. Bientôt, vous sombrez dans un profond sommeil tandis que
la toile de la tente claque sous la puissance du vent. Votre nuit,
cependant, est peuplée de cauchemars dans lesquels Vonotar le
Traître vous apparaît en une succession d'images terrifiantes.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome3/page_291.py", label="291", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
