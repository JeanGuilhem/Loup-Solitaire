import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import stream_text, called_cookies, hazard_roll

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=201, book=2)

fr_text = """
Lorsque vous bondissez sur vos pieds, le serpent siffle et tente de vous
mordre au bras. Vous faites un pas de côté pour l'éviter mais avez-vous
été suffisamment rapide pour échapper à ses crochets mortels ?
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    number = hazard_roll()
    if number is not None and number <= 4:
        st.page_link("tomes/tome2/page_285.py", label="285", icon="📄")
    elif number is not None:
        st.page_link("tomes/tome2/page_70.py", label="70", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
