import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    receive_gold,
    remove_from_inventory,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=165, book=2)

fr_text = """
Vous rangez l'or dans votre bourse, puis vous ôtez l'Anneau de votre
doigt et vous le lui tendez. Elle vous le prend des mains et l'examine
attentivement. Vous quittez ensuite la boutique mais au moment où
vous franchissez la porte, vous l'entendez ricaner sous cape et vous
vous demandez alors si vous avez bien fait d'agir ainsi.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        # la vieille femme (§289) vous a acheté le Sceau d'Hammardal 40 Pièces d'Or
        remove_from_inventory("SCEAU D'HAMMARDAL")
    receive_gold(40)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_186.py", label="186", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
