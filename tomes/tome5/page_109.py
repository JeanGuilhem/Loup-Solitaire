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

check_inventory(current_page_number=109, book=5)

fr_text = """
Vous sautez dans la rue en contrebas, puis vous traversez en
courant la place du Marché vers le bâtiment à l'intérieur duquel
sont regroupés des centaines d'habitants en prières. Vous
apercevez une avenue à votre droite qui se termine par un porche
voûté sous lequel ne peut s'engager qu'un seul cheval. A votre
gauche, une autre allée descend vers le port.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez entrer dans le bâtiment, rendez-vous au :"))
    st.page_link("tomes/tome5/page_32.py", label="32", icon="📄")

    st.write_stream(stream_text("Si vous voulez tourner à droite et atteindre le porche, rendez-vous au :"))
    st.page_link("tomes/tome5/page_169.py", label="169", icon="📄")

    st.write_stream(stream_text("Si vous décidez de retourner au port, rendez-vous au :"))
    st.page_link("tomes/tome5/page_129.py", label="129", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
