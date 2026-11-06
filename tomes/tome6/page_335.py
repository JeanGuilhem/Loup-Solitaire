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

check_inventory(current_page_number=335, book=6)

fr_text = """
Avec un craquement sec et sonore votre Jakan se brise en deux.
Un immense éclat de rire s'élève des tribunes et le sévère Altan
lui-même a du mal à garder son sérieux au spectacle que vous
offrez. Le petit homme au pourpoint galonné annonce que vous
avez perdu le tournoi par abandon et Altan est proclamé
vainqueur. La foule des villageois se précipite vers Altan pour le
congratuler. Vous en profitez pour disparaître et rejoindre
Cyrilus et vos montures.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome6/page_33.py", label="33", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
