import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies, ls_death

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=8, book=2)

fr_text = """
A la vérité, vous êtes plongé dans un sommeil si profond que vous ne
vous réveillerez jamais plus car au cours de la nuit un Serpent des
Sables vous a mordu et son venin mortel a eu raison de vous en
quelques secondes. Votre mission s'achève ici, en même temps que
votre vie.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    show_illustrations()
    ls_death()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
