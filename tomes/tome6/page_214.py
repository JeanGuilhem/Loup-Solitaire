import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    set_flag,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=214, book=6)

fr_text = """
L'arc de chasse de Kalte est fait de plusieurs os, soudés entre eux
par des fibres tendineuses. C'est une arme idéale pour chasser le
Baknar ou le Kalkoth dans les immensités glacées du Pays de
Kalte mais, comme arc de tir dans les Terres de la Storn au
climat chaud, c'est une arme peu efficace. Avant de commencer
le tournoi, vous devez en conséquence réduire votre total
d'HABILETÉ de 4 points pour la durée de la compétition.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # Fait posé : « arc de Kalte » (-4 HABILETÉ pendant le tournoi, paragraphes 340 et 26)
    if is_new_page():
        set_flag("arc emprunté")
        set_flag("arc de Kalte")
    st.info("Vous tirez avec l'arc de Kalte : -4 points d'HABILETÉ pendant toute la durée du tournoi.")

    st.write_stream(stream_text("Pour commencer le tournoi, rendez-vous au :"))
    st.page_link("tomes/tome6/page_340.py", label="340", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
