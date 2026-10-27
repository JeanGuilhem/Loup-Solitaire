import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=112, book=2)

fr_text = """
Vous vous rappelez soudain ce qu'il vous a dit au sujet de la boutique à
la porte orange. C'est le Quartier Général de la Fraternité du Silence, la
célèbre police secrète de Lachelan. Entrer dans cette boutique serait
plus dangereux encore que de pénétrer dans une pièce remplie de
Drakkarim ! Vous vous détournez aussitôt de la porte orange et vous
vous hâtez en direction du nord.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_230.py", label="230", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
