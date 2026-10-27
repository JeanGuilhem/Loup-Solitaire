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

check_inventory(current_page_number=273, book=2)

fr_text = """
Vous vous apprêtez à frapper, mais votre adversaire s'écrie: «Je suis
Ronan, my lord, et je ne vous veux aucun mal ! » Vous détournez votre
coup de justesse et votre arme s'abat dans le vide. La sueur qui perle sur
le visage du marin semble confirmer qu'il dit bien la vérité.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rengainez votre arme et rendez-vous au :'))
    st.page_link("tomes/tome2/page_160.py", label="160", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
