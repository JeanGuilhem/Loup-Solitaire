import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=135, book=3)

fr_text = """
Vous glissez le Disque dans la fente ; il s'y adapte exactement et
la porte s'ouvre. Dès que vous l'avez franchie, cependant, elle se
referme derrière vous. Vous vous retrouvez dans un petit couloir
qui mène à une arcade masquée par des rideaux. Vous les écartez
avec précaution et vous découvrez alors une vaste salle. Vous
avez été bien avisé d'être si prudent : à moins de 3 mètres de
vous, en effet, se tient Vonotar le Traître. Deux Barbares des
Glaces sont debout devant lui et il est en train de leur passer au
poignet des bracelets d'or.
A présent que la porte s'est refermée dans votre dos, il ne vous
reste plus qu'à attaquer Vonotar par surprise pour essayer de le
capturer. Vous armant de courage, vous vous précipitez donc en
avant.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome3/page_100.py", label="100", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
