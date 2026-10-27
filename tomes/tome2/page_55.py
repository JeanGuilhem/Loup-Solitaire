import streamlit as st
from inventory import (
    buy_button,
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

check_inventory(current_page_number=55, book=2)

fr_text = """
Un homme de haute taille vêtu d'un tablier de cuir est en train d'aiguiser
un glaive de belle apparence. L'homme est assis devant une meule qui
projette des gerbes d'étincelles chaque fois que la lame de l'épée entre
en contact avec la pierre. Le forgeron vous souhaite le bonsoir et vous
offre le glaive. « C'est une belle lame, dit-il, forgée dans un pur acier de
Durenor. Pour douze Couronnes, elle est à vous. »
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez acheter ce glaive :"))
    buy_button("GLAIVE", 12, key="glaive", label="Acheter le Glaive (12 Couronnes)")

    st.write_stream(
        stream_text(
            "Si vous décidez de quitter la boutique par la porte principale, rendez-vous au :"
        )
    )
    st.page_link("tomes/tome2/page_347.py", label="347", icon="📄")

    st.write_stream(stream_text("Si vous préférez passer par la porte de derrière, rendez-vous au :"))
    st.page_link("tomes/tome2/page_3.py", label="3", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
