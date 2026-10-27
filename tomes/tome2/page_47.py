import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=47, book=2)

fr_text = """
Les soldats se hâtent de descendre du toit et empoignent leurs lances ;
puis ils s'avancent vers vous. « Le mot de passe, étranger ! » crie l'un
d'eux.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous connaissez le mot de passe qui permet de franchir le pont, rendez-vous au :"))
    st.page_link("tomes/tome2/page_111.py", label="111", icon="📄")
    st.write_stream(stream_text("Sinon, rendez-vous au :"))
    st.page_link("tomes/tome2/page_307.py", label="307", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
