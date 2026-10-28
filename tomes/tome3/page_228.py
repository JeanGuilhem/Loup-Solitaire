import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=228, book=3)

fr_text = """
Vous faites appel à tous vos pouvoirs de concentration pour
élever le bol d'herbes fumantes et le faire avancer dans le couloir,
suspendu dans les airs. Enfin, vous le posez à distance à l'ombre
d'un pilastre et vous observez avec une grande curiosité les effets
produits par la mixture. Moins d'une minute plus tard, les
Barbares des Glaces se sont effondrés sur le sol. «Allons-y à
présent», murmure Loi-Kymar en vous faisant sortir de la
cuisine. Vous vous approchez ensuite de la salle du Trône du
Brumalmarc et vous découvrez alors que l'une des magnifiques
portes incrustées de pierreries n'est pas fermée à clé. Tirant
aussitôt votre épée, vous entrebâillez doucement la porte et vous
pénétrez dans le repaire de Vonotar.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome3/page_173.py", label="173", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
