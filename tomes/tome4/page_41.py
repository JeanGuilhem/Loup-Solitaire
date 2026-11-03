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

check_inventory(current_page_number=41, book=4)

fr_text = """
Vous reconnaissez cette sécrétion gluante : c'est la trace
caractéristique d'un Ver de Pierre, un prédateur souterrain
particulièrement redoutable. Vous recommandez à vos hommes
de ne pas marcher dans ce liquide qui est extrêmement acide,
mais à peine avez-vous prononcé ces mots qu'un bruit terrifiant
retentit soudain.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome4/page_276.py", label="276", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
