import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    receive_gold,
    show_illustrations,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=329, book=2)

fr_text = """
« Félicitations, Loup Solitaire, dit bientôt le capitaine en essuyant la
sueur qui perle à son front, vous êtes un joueur de première force et
vous avez gagné. » Il fouille dans une poche de son gilet et vous tend
une bourse contenant 10 Pièces d'Or. Vous le remerciez d'avoir joué
avec vous et vous lui proposez de prendre sa revanche le lendemain
soir. Avec un sourire quelque peu amer, il accepte votre offre et vous
souhaite bonne nuit.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    receive_gold(10)

    st.write_stream(stream_text("Rentrez dormir dans votre cabine, à présent, en vous rendant au :"))
    st.page_link("tomes/tome2/page_197.py", label="197", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
