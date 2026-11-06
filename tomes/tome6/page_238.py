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

check_inventory(current_page_number=238, book=6)

fr_text = """
Vous venez de parcourir une centaine de mètres vers la porte est
par laquelle vous êtes entré, lorsque vous remarquez une plaque
de cuivre rutilante fixée par de gros clous au-dessus d'un porche
voûté. Vous pouvez lire :
GUILDE DES CRIEURS PUBLICS
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez descendre de cheval et pénétrer sous le porche, rendez-vous au :"))
    st.page_link("tomes/tome6/page_25.py", label="25", icon="📄")

    st.write_stream(stream_text("Sinon, continuez votre chemin vers la porte est d'où partent les deux rues."))
    st.write_stream(stream_text("Si vous souhaitez prendre la rue qui se dirige vers le nord, rendez-vous au :"))
    st.page_link("tomes/tome6/page_79.py", label="79", icon="📄")

    st.write_stream(stream_text("Si vous préférez suivre la rue vers le sud, rendez-vous au :"))
    st.page_link("tomes/tome6/page_147.py", label="147", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
