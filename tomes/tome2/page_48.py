import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=48, book=2)

fr_text = """
Vous désignez du doigt une chope de bière posée sur le bar et vous
demandez au marin de l'observer attentivement. Vous fermez alors les
yeux et vous vous concentrez jusqu'à ce que l'image de la chope se
forme dans votre esprit. Sous l'effet de votre volonté, la chope s'élève
bientôt dans les airs sous le regard médusé de votre interlocuteur.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_268.py", label="268", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
