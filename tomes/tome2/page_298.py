import streamlit as st
from combat import combat
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

check_inventory(current_page_number=298, book=2)

fr_text = """
Vous entendez derrière vous leurs pas se précipiter et vous faites
brusquement volte-face, au moment même où ils dégainent chacun un
poignard pour vous attaquer. Si vous n'avez pas d'armes, vous devrez
déduire 4 points de votre total d'ENDURANCE et les combattre à
mains nues. Vous les affronterez un par un.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Vous avez le droit de prendre la fuite à tout moment en vous rendant au 121. Si vous parvenez à tuer les trois voleurs, rendez-vous au 301.'))
    outcome = combat(
        [("Chef des VOLEURS", 15, 23), ("1er VOLEUR", 13, 21), ("2e VOLEUR", 13, 20)],
        flee_after=0,
    )
    if outcome == "win":
        st.page_link("tomes/tome2/page_301.py", label="301", icon="📄")
    elif outcome == "fled":
        st.page_link("tomes/tome2/page_121.py", label="121", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
