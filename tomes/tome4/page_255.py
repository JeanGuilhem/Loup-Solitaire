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

check_inventory(current_page_number=255, book=4)

fr_text = """
Il vous faut rassembler les défenseurs sommerlundais, sinon tout
est perdu. Vous ordonnez à deux soldats de porter secours au
capitaine, puis vous sautez sur un wagon retourné pour observer
l'avance des ennemis. Ils ont déjà atteint le périmètre en ruine de
Ruanon et poursuivent leur approche à l'abri des murs encore
debout. Vous donnez l'ordre aux soldats du capitaine Gayal de
défendre la barricade, mais les Guerriers ennemis ne sont plus
qu'à une centaine de mètres et peut-être est-il déjà trop tard pour
repousser leur attaque.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome4/page_186.py", label="186", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
