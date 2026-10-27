import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=303, book=2)

fr_text = """
Des amas d'ordures pourrissantes ont été déversés sur cette partie du
quai et l'odeur qui s'en dégage est si pestilentielle que vous vous
couvrez la bouche et le nez d'un pan de votre cape. Un peu plus loin sur
votre gauche, vous apercevez la lueur d'une torche qui filtre par une
porte ouverte. Une enseigne est accrochée au-dessus de la porte et porte
cette inscription :

GRAND MAGASIN DE RAGADORN — ACHAT, VENTE, ÉCHANGE
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez entrer dans le magasin, rendez-vous au :"))
    st.page_link("tomes/tome2/page_173.py", label="173", icon="📄")
    st.write_stream(stream_text("Si vous préférez poursuivre en direction du sud, rendez-vous au :"))
    st.page_link("tomes/tome2/page_18.py", label="18", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
