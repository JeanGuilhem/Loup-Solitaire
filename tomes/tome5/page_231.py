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

check_inventory(current_page_number=231, book=5)

fr_text = """
Les Drakkars se précipitent dans la salle des Gardes en
mugissant comme des Mammouths de Kalte et en battant l'air de
leurs terrifiantes épées noires. Leur chef avance vers vous, une
longue mèche de cheveux d'un noir de jais s'échappant de son
heaume, l'épée prête à vous donner le coup qui vous étripera.
Mais vous faites un pas de côté et vous lui assénez un violent
coup en pleine poitrine. Votre arme enfonce le métal noir de sa
cuirasse, lui écrasant les côtes et le tuant sur le coup ; mais avant
même qu'il ne s'écroule au sol, deux autres Drakkars sont sur
vous. Vous ne pouvez pas éviter le combat et vous devez les
combattre jusqu'à ce que mort s'ensuive.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("DRAKKARS", 18, 34)])
    if outcome == "win":
        st.write_stream(stream_text("Si vous remportez le combat, rendez-vous au :"))
        st.page_link("tomes/tome5/page_290.py", label="290", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
