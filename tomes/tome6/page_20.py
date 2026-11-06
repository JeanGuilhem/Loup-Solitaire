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

check_inventory(current_page_number=20, book=6)

fr_text = """
Votre embuscade prend l'ennemi au dépourvu et vos adversaires, en
proie à la panique la plus totale, se dispersent dans toutes les
directions. A une si courte distance, il vous est impossible de
manquer une cible, et votre flèche va se planter dans la poitrine
du cavalier qui tient le cheval de Cyrilus par la bride. L'homme
s'effondre raide mort sur le sol, et vous en profitez aussitôt
pour surgir des broussailles et saisir les rênes du cheval de
votre victime. Des cris de colère retentissent derrière vous
tandis que vous vous éloignez au triple galop, en compagnie du
vieux magicien.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_188.py", label="188", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
