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

check_inventory(current_page_number=282, book=2)

fr_text = """
De la pointe de leurs lances, les SOLDATS essaient de vous repousser.
Et tandis que vous levez votre arme sur l'un d'eux, l'autre vous
contourne pour vous attaquer par-derrière. Il vous est impossible de
prendre la fuite et vous allez devoir les combattre à tour de rôle jusqu'à
la mort.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("1er SOLDAT DU PONT", 16, 24), ("2e SOLDAT DU PONT", 16, 22)])
    if outcome == "win":
        st.write_stream(stream_text("Si vous êtes vainqueur, rendez-vous au :"))
        st.page_link("tomes/tome2/page_187.py", label="187", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
