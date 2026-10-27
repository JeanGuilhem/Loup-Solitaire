import streamlit as st
from inventory import (
    add_to_inventory,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=103, book=2)

fr_text = """
Le Laumspur est une herbe délicieuse très recherchée d'un bout à l'autre
des Fins de Terre en raison de ses vertus curatives. Vous en avez
ramassé l'équivalent d'un Repas et ce Repas vous rendra 3 points
d'ENDURANCE lorsque vous le prendrez (inscrivez sur votre Feuille
d'Aventure : moisson de Laumspur). Vous enveloppez
soigneusement l'herbe que vous venez de ramasser et vous retournez
dans la diligence en compagnie des autres voyageurs.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        add_to_inventory("MOISSON DE LAUMSPUR")
    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_249.py", label="249", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
