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

check_inventory(current_page_number=31, book=3)

fr_text = """
La statue se dresse lentement sur l'autel et s'avance vers vous.
Tandis qu'elle s'approche, vous sentez un froid intense rayonner
de sa surface de pierre lisse. Ses mouvements, cependant, sont
raides et imprécis ; il ne vous serait pas difficile d'éviter ses bras
tendus.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez attaquer cette étrange statue, rendez-vous au :'))
    st.page_link("tomes/tome3/page_150.py", label="150", icon="📄")

    st.write_stream(
        stream_text(
            "Si vous préférez la contourner et courir vers l'arcade qui se trouve derrière elle, "
            'rendez-vous au :'
        )
    )
    st.page_link("tomes/tome3/page_306.py", label="306", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
