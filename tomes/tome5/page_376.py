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

check_inventory(current_page_number=376, book=5)

fr_text = """
Vous suivez la rue pendant quelques mètres avant d'arriver
devant une longue bâtisse aux murs blanchis à la chaux et percés
de petites fenêtres étroites et sinistres. Un Garde, assis sur le
trottoir, somnole au soleil couchant, sa lance entre les jambes.
Quelques enfants lui lancent des fruits de larnumier pourris en
visant l'extrémité de sa lance. En face du bâtiment, devant une
taverne, sont alignés plusieurs Douggas sellés et attachés par
leurs rênes à un poteau près de l'entrée. Les cris de ces chevaux
du désert rivalisent avec les rumeurs joyeuses qui parviennent de
l'intérieur de l'auberge.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez entrer dans la taverne, rendez-vous au :"))
    st.page_link("tomes/tome5/page_351.py", label="351", icon="📄")
    st.write_stream(stream_text("Si vous préférez continuer vers le marché aux Douggas, rendez-vous au :"))
    st.page_link("tomes/tome5/page_202.py", label="202", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
