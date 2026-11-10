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

check_inventory(current_page_number=201, book=7)

fr_text = """
Vous vous hâtez le long du tunnel et vous arrivez bientôt dans
une pièce éclairée par une lumière rouge et scintillante,
provenant d'une ouverture carrée dans le plafond. Une immense
porte en fer à deux battants occupe tout le mur du fond mais,
pour l'atteindre, vous devrez traverser cet inquiétant faisceau de
lumière rouge. Près de l'entrée, par laquelle vous êtes arrivé, se
trouve un autre tunnel qui s'enfonce en serpentant vers l'est.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez passer à travers la lumière rouge pour examiner les portes en fer, rendez-vous au :"))
    st.page_link("tomes/tome7/page_269.py", label="269", icon="📄")

    st.write_stream(stream_text("Si vous préférez quitter la pièce par le tunnel est, rendez-vous au :"))
    st.page_link("tomes/tome7/page_272.py", label="272", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
