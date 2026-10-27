import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=56, book=2)

fr_text = """
L'aubergiste vous tend une clé. « Chambre 4, deuxième porte à gauche
en haut de l'escalier», annonce-t-il. Il faudra libérer les lieux une heure
après le lever du soleil. Votre chambre n'est meublée que d'un lit, d'une
chaise et d'une petite table. Avant d'aller vous coucher, vous verrouillez
la porte et vous coincez la chaise contre le panneau par mesure de
sécurité. Dès demain, vous établirez un nouvel itinéraire pour rejoindre
le royaume de Durenor.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_127.py", label="127", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
