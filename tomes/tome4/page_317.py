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

check_inventory(current_page_number=317, book=4)

fr_text = """
Vous concentrez vos pouvoirs sur une saillie d'argile qui
surplombe le puits, de l'autre côté de la salle. Quelques secondes
plus tard, le bloc se détache dans un craquement et tombe au
fond du trou béant. Surpris par ce bruit soudain, le Garde quitte
son poste pour aller voir de quoi il retourne. Sans hésiter un
instant, vous vous précipitez vers le pont qui n'est plus surveillé
et vous le franchissez, disparaissant dans le tunnel situé de
l'autre côté.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome4/page_348.py", label="348", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
