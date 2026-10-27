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

check_inventory(current_page_number=177, book=2)

fr_text = """
Lorsque vous entrez à nouveau dans la taverne, vous voyez les marins
rassemblés autour d'une table où se déroule une partie de bras de fer.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez vous aussi engager une partie de bras de fer, rendez-vous au :"))
    st.page_link("tomes/tome2/page_276.py", label="276", icon="📄")

    st.write_stream(stream_text("Si vous préférez parler à l'aubergiste, rendez-vous au :"))
    st.page_link("tomes/tome2/page_342.py", label="342", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
