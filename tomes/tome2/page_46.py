import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=46, book=2)

fr_text = """
Vous vous efforcez de vous rappeler la signification de cette porte
orange, mais sans succès.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous décidez d'entrer dans la boutique, rendez-vous au :"))
    st.page_link("tomes/tome2/page_214.py", label="214", icon="📄")
    st.write_stream(stream_text("Si vous préférez poursuivre votre chemin, rendez-vous au :"))
    st.page_link("tomes/tome2/page_230.py", label="230", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
