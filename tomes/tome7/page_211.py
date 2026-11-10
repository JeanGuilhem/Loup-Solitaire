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

check_inventory(current_page_number=211, book=7)

fr_text = """
Le seul moyen de franchir le vide serait d'escalader la paroi
rocheuse, mais elle est pratiquement verticale, et tenter une telle
escalade sans équipement approprié serait extrêmement
dangereux.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez, néanmoins, essayer de grimper à la paroi, rendez-vous au :"))
    st.page_link("tomes/tome7/page_85.py", label="85", icon="📄")

    st.write_stream(stream_text("Si vous préférez descendre l'escalier et continuer ensuite le long de la plage, rendez-vous au :"))
    st.page_link("tomes/tome7/page_348.py", label="348", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
