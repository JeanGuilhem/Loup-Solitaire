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

check_inventory(current_page_number=152, book=6)

fr_text = """
Vous convenez de retrouver le Capitaine à l'herboristerie dans
une heure, puis vous partez explorer Luyen. Un peu plus loin
dans la rue, vous arrivez devant une vitrine poussiéreuse où sont
entassées des armes de toutes sortes. Au-dessus de la porte est
accrochée une enseigne :
DEMICO ARMURIER ACHAT ET VENTE D'ARMES EN TOUT
GENRE
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez entrer dans ce magasin d'armes d'occasion, rendez-vous au :"))
    st.page_link("tomes/tome6/page_98.py", label="98", icon="📄")

    st.write_stream(stream_text("Si vous préférez continuer à remonter la rue, rendez-vous au :"))
    st.page_link("tomes/tome6/page_275.py", label="275", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
