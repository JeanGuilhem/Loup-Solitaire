import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=68, book=2)

fr_text = """
Le garde vous jette un regard méprisant. « Je suis un soldat de Durenor,
dit-il, et votre or ne vous sera d'aucun secours avec moi. » Vous avez
eu le tort de porter atteinte à son honneur et il vous donne une rude
leçon.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_306.py", label="306", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
