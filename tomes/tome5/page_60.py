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

check_inventory(current_page_number=60, book=5)

fr_text = """
Vous bondissez sur le premier guerrier en feignant de le frapper
par la gauche. Ceci vous permet d'anticiper sa réaction et de le
prendre à contre-pied. Plié en deux par la douleur, votre
adversaire titube et tombe à la renverse dans le cloaque. Ses
compagnons semblent hésiter et reculent d'un pas. Soudain, une
voix tonitruante emplit le souterrain : « Laissez-le-moi, bande
d'imbéciles ! » Il s'agit de Maouk, qui sort de l'ombre en
brandissant une fléchette. Il pousse un juron entre ses dents,
puis il vous lance son projectile en pleine poitrine.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome5/page_25.py", label="25", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
