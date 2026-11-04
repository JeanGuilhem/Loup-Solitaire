import streamlit as st
from combat import combat
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=4, book=5)

fr_text = """
Vous vous penchez pour saisir l'épée, mais le deuxième Garde
passe à l'attaque au moment où vos doigts se referment sur la
garde.
Durant le premier Assaut, votre adversaire ne peut pas perdre de
point d'ENDURANCE, car vous ne pouvez qu'essayer de parer le
coup qu'il vous destine.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # le Geôlier ne perd aucun point d'ENDURANCE au premier Assaut
    outcome = combat([("GEÔLIER DU PALAIS", 14, 21)], enemy_immune_rounds=1)
    if outcome == "win":
        if st.session_state["combat_combat"]["round"] <= 4:
            st.write_stream(stream_text('Si vous gagnez le combat en 4 Assauts ou moins, rendez-vous au :'))
            st.page_link("tomes/tome5/page_165.py", label="165", icon="📄")
        else:
            st.write_stream(stream_text('Si le combat dure plus de 4 Assauts, rendez-vous au :'))
            st.page_link("tomes/tome5/page_180.py", label="180", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
