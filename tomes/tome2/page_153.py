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

check_inventory(current_page_number=153, book=2)

fr_text = """
Vous laissez le fripon à ses tasses et à sa bille, et vous vous approchez
d'un groupe d'hommes qui jouent aux cartes près de l'escalier de la
taverne. Au bout d'un moment, vous vous apercevez que l'un des
joueurs est en train de tricher.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez défier cet homme, rendez-vous au :"))
    st.page_link("tomes/tome2/page_241.py", label="241", icon="📄")

    st.write_stream(stream_text("Si vous préférez ne pas vous en mêler, rendez-vous au :"))
    st.page_link("tomes/tome2/page_130.py", label="130", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
