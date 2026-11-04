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

check_inventory(current_page_number=295, book=5)

fr_text = """
Concentrant toute votre volonté sur la bourse qui est accrochée à
la ceinture de la sentinelle, vous essayez d'en dénouer les
cordons de cuir. Quelques secondes plus tard, la bourse tombe
sur le sol en répandant tout son contenu. Le Garde pousse un cri
en voyant son or rouler par-dessus le bord de la plate-forme et se
met précipitamment à genoux pour ramasser le peu qui reste.
Tandis qu'il vous tourne le dos, vous vous élancez à découvert
pour traverser la passerelle.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome5/page_236.py", label="236", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
