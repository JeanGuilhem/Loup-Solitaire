import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=258, book=7)

fr_text = """
La faible lueur du bouclier protecteur est l'unique source de
lumière dans la grotte. Vous avancez prudemment mais vous êtes
bientôt complètement environné par les ténèbres et vous
progressez très lentement.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    light = has_item("SPHÈRE DE FEU") or has_item("LANTERNE") or has_item("TORCHE") or has_item("BRIQUET À AMADOU")
    st.write_stream(stream_text("Si vous possédez une Sphère de Feu de Kalte, une Lanterne, une Torche ou un Briquet d'Amadou, rendez-vous au :"))
    st.page_link("tomes/tome7/page_49.py", label="49", icon="📄", disabled=not light)

    st.write_stream(stream_text("Si vous ne possédez aucun de ces objets et que vous souhaitez néanmoins continuer à avancer dans l'obscurité totale, rendez-vous au :"))
    st.page_link("tomes/tome7/page_277.py", label="277", icon="📄", disabled=light)

    st.write_stream(stream_text("Si vous préférez quitter la grotte et retourner sur la plage, rendez-vous au :"))
    st.page_link("tomes/tome7/page_30.py", label="30", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
