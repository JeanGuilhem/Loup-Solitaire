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

check_inventory(current_page_number=48, book=3)

fr_text = """
Le Barbare des Glaces passe à une quinzaine de centimètres de
votre cachette. Il s'arrête un instant, puis revient sur ses pas le
long du couloir. Vous poussez alors un soupir de soulagement : il
ne vous a pas découvert.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(
        stream_text(
            'Si vous souhaitez vous enfuir sur la pointe des pieds par le couloir orienté au nord, '
            'rendez-vous au :'
        )
    )
    st.page_link("tomes/tome3/page_215.py", label="215", icon="📄")

    st.write_stream(
        stream_text(
            'Si vous préférez attaquer le Barbare des Glaces par derrière, rendez-vous au :'
        )
    )
    st.page_link("tomes/tome3/page_260.py", label="260", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
