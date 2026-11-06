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

check_inventory(current_page_number=342, book=6)

fr_text = """
Vous descendez de votre cheval et vous vous dirigez vers la serre.
« Bienvenue, monseigneur, bienvenue à la Serre Sacrée des
Guerriers, vous dit une matrone aux joues rouges en essuyant
une feuille avec un carré de soie. Les fruits de nos plantes
d'Alether vous redonneront force et vigueur dans la bataille. »
Elle vous tend une poignée de baies orangées.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous acceptez d'acheter quelques baies d'Alether, rendez-vous au :"))
    st.page_link("tomes/tome6/page_123.py", label="123", icon="📄")

    st.write_stream(stream_text('Si vous préférez décliner son offre, vous remontez à cheval et vous quittez le village (rendez-vous au :'))
    st.page_link("tomes/tome6/page_100.py", label="100", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
