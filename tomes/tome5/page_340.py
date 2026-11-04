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

check_inventory(current_page_number=340, book=5)

fr_text = """
Pendant une heure, vous courez à travers toute la ville d'Ikaresh
avec les Adu-Kaws à vos trousses. Vous parvenez à leur faire
perdre vos traces grâce à Banedon qui, par une formule magique,
vous a transformés tous deux en Kalkoths. Heureusement, vos
poursuivants n'ont pas cherché à comprendre pourquoi,
brusquement, deux monstres des Grottes de Kalte parcouraient
ainsi les rues de leur propre ville ! Une fois remis de cette longue
poursuite, vous quittez l'allée étroite où vous vous étiez cachés et
vous vous remettez rapidement à la recherche de Tipasa le Vagabond.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome5/page_202.py", label="202", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
