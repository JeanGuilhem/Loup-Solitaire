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

check_inventory(current_page_number=28, book=3)

fr_text = """
Essuyant le sang qui vous a éclaboussé le visage, vous sortez de la
cellule d'un pas chancelant et vous pénétrez dans le couloir. Au
loin, vous apercevez une bifurcation.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(
        stream_text(
            'Si vous souhaitez fouiller le cadavre du Barbare des Glaces, il va falloir le traîner '
            'dans la lumière du couloir en vous rendant au :'
        )
    )
    st.page_link("tomes/tome3/page_210.py", label="210", icon="📄")

    st.write_stream(
        stream_text(
            'Si vous préférez poursuivre votre mission aussi rapidement que possible, refermez la '
            "porte de la cellule et avancez le long du couloir jusqu'à la bifurcation. Rendez-vous "
            'pour cela au :'
        )
    )
    st.page_link("tomes/tome3/page_215.py", label="215", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
