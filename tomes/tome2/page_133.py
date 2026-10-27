import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=133, book=2)

fr_text = """
Vous regardez le marin droit dans les yeux et vous concentrez votre
Puissance Psychique sur sa main ouverte. Soudain, l'homme tombe de
sa chaise en se tenant la main et en hurlant comme s'il venait de saisir
des charbons ardents. Lorsque vous lui expliquez que seul votre
pouvoir a provoqué cette douleur, il vous contemple d'un air stupéfait.
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
