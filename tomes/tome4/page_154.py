import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=154, book=4)

fr_text = """
Lorsque vous êtes certain que les bandits ne vous poursuivent
plus, vous vous arrêtez pour rassembler vos soldats épuisés. Dix
hommes seulement ont échappé à la bataille, les autres ont été
soit capturés, soit tués avant d'avoir pu s'enfuir. A présent que la
route qui mène au Sommerlund est coupée par les bandits, vous
n'avez d'autre choix que de continuer vers le sud.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    roll = hazard_roll()
    if roll is not None and roll <= 2:
        st.write_stream(stream_text('Si vous tirez le 0, le 1 ou le 2, rendez-vous au :'))
        st.page_link("tomes/tome4/page_120.py", label="120", icon="📄")
    elif roll is not None:
        st.write_stream(stream_text('Si vous tirez un chiffre entre 3 et 9, rendez-vous au :'))
        st.page_link("tomes/tome4/page_51.py", label="51", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
