import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import stream_text, called_cookies, ls_death

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=212, book=2)

fr_text = """
Le malheur veut que vous n'ayez pas d'armes et qu'il soit lui-même un
redoutable bretteur. Le combat est désespéré et fort bref. Il vous
transperce d'un coup d'épée et vous jette à bas du chariot d'un simple
coup de pied. Mais rassurez-vous, votre chute ne sera pas trop
douloureuse car vous êtes déjà mort lorsque vous arrivez en bas. Votre
mission s'achève ici en même temps que votre vie.
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
