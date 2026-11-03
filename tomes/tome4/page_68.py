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

check_inventory(current_page_number=68, book=4)

fr_text = """
Il vous suffit de frapper la serrure d'un coup sec de la main pour
forcer la porte du hangar à bateaux. Vous apercevez alors un
bateau à rames retourné sur des tréteaux. Un seau de poix est
posé au-dessous. A en juger par la couche de poussière qui
couvre la coque du bateau, il semble qu'il soit resté là pendant
plusieurs mois.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez mettre ce bateau à l'eau, rendez-vous au :"))
    st.page_link("tomes/tome4/page_180.py", label="180", icon="📄")

    st.write_stream(stream_text("Si vous préférez fouiller le hangar dans l'espoir d'y trouver des objets utiles, rendez-vous au :"))
    st.page_link("tomes/tome4/page_213.py", label="213", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
