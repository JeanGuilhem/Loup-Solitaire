import streamlit as st
from inventory import (
    buy_button,
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

check_inventory(current_page_number=275, book=6)

fr_text = """
Au bout de la rue, vous vous arrêtez pour regarder la vitrine
d'une grande boutique. A l'intérieur se trouve toute une
collection fascinante de cartes et de plans détaillés des diverses
régions et cités du Magnamund. Vous entrez dans le magasin et
examinez les étagères qui tapissent les murs. Trois cartes en
particulier attirent votre attention: une Carte du Sommerlund (5
Pièces d'Or), une Carte de Tekaro (4 Pièces d'Or) et une Carte de
Luyen (3 Pièces d'Or). Ces cartes sont des Objets de Sac à Dos. Si
vous souhaitez acquérir l'une ou l'autre de ces cartes ou les
trois, notez vos achats sur votre Feuille d'Aventure avant de
retourner à l'Herboristerie.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    buy_button("CARTE DU SOMMERLUND", 5, key="t6_275_sommerlund", label="Acheter la Carte du Sommerlund (5 Pièces d'Or)")
    buy_button("CARTE DE TEKARO", 4, key="t6_275_tekaro", label="Acheter la Carte de Tekaro (4 Pièces d'Or)")
    buy_button("CARTE DE LUYEN", 3, key="t6_275_luyen", label="Acheter la Carte de Luyen (3 Pièces d'Or)")

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_231.py", label="231", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
