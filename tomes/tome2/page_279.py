import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=279, book=2)

fr_text = """
Cette créature est un Noudic. Les Noudics sont des êtres doués
d'intelligence qui vivent dans un dédale de puits et de couloirs creusés
au sein des Monts d'Hammardal. De tempérament malicieux, ils
subsistent en volant de la nourriture dans les chariots des marchands
qui empruntent le tunnel de Tarnalin.
Les Noudics pourraient peut-être vous renseigner sur la présence
éventuelle de Monstres d'Enfer cachés dans le tunnel.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez suivre cet animal, rendez-vous au :'))
    st.page_link("tomes/tome2/page_23.py", label="23", icon="📄")

    st.write_stream(stream_text('Si vous préférez le laisser filer et poursuivre votre chemin, rendez-vous au :'))
    st.page_link("tomes/tome2/page_340.py", label="340", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
