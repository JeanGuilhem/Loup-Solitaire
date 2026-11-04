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

check_inventory(current_page_number=106, book=5)

fr_text = """
Vous vous laissez tomber lourdement sur le cavalier puis vous
l'entraînez au sol, mais votre réception est maladroite et vous
devez le relâcher. Le Messager est le premier à se remettre sur
pieds ; il dégaine son épée et attaque avant même que vous
n'ayez eu le temps de vous relever.
Ôtez 2 points à votre total d'HABILETÉ pour les 3 premiers
Assauts car vous êtes toujours au sol. Vous n'avez aucune
possibilité de fuite et vous devez combattre le Messager jusqu'à la
mort.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # toujours au sol pendant les 3 premiers assauts : -2 HABILETÉ
    outcome = combat([("MESSAGER", 16, 23)], first_round_modifier=-2, first_rounds=3)
    if outcome == "win":
        st.write_stream(stream_text("Si vous sortez vainqueur, rendez-vous au :"))
        st.page_link("tomes/tome5/page_189.py", label="189", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
