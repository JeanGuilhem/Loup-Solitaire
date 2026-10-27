import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=89, book=2)

fr_text = """
Au moment où vous sautez, le conducteur vous aperçoit et arrête
aussitôt la diligence. Puis il se tourne vers vous, une épée à la main.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez lui payer le prix d'un billet, rendez-vous au :"))
    st.page_link("tomes/tome2/page_233.py", label="233", icon="📄")

    st.write_stream(stream_text("Si vous préférez l'attaquer, rendez-vous au :"))
    st.page_link("tomes/tome2/page_212.py", label="212", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
