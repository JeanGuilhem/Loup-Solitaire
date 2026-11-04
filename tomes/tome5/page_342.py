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

check_inventory(current_page_number=342, book=5)

fr_text = """
Une délicieuse odeur de vin de Jala fraîchement tiré parvient
jusqu'à vous depuis une auberge située au milieu de l'avenue.
Des bribes de conversations, mêlées à des tintements de verres
qu'on entrechoque, ainsi que les cris d'un bébé affamé
remplissent l'air.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez entrer dans l'auberge, rendez-vous au :"))
    st.page_link("tomes/tome5/page_296.py", label="296", icon="📄")

    st.write_stream(stream_text("Si vous préférez continuer à marcher dans l'avenue, rendez-vous au :"))
    st.page_link("tomes/tome5/page_227.py", label="227", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
