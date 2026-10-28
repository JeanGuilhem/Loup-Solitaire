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

check_inventory(current_page_number=13, book=3)

fr_text = """
Il y a un levier dans le mur et un judas au milieu de la porte. En
jetant un coup d'œil à travers le judas, vous découvrez un étrange
spectacle : un homme vêtu d'une toge sombre est agenouillé au
centre d'un pentacle dessiné à la craie sur le sol d'une cellule. Il a
la tête penchée et semble en transe.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez tirer le levier et ouvrir la porte, rendez-vous au :'))
    st.page_link("tomes/tome3/page_128.py", label="128", icon="📄")

    st.write_stream(
        stream_text(
            'Si vous préférez laisser cet homme où il est et poursuivre votre exploration du couloir '
            'principal, rendez-vous au :'
        )
    )
    st.page_link("tomes/tome3/page_254.py", label="254", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
