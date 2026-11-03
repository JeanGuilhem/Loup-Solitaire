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

check_inventory(current_page_number=26, book=4)

fr_text = """
Tandis que vous courez vers l'échelle, vous entendez les cris
épouvantables de vos hommes en train de mourir dévorés
vivants. Vous vous immobilisez et vous jetez un coup d'œil
derrière vous, dans le tunnel. Le Ver de Pierre est maintenant à 5
mètres environ et ondule dans votre direction à une allure
terrifiante. Il est clair que vous n'atteindrez pas l'échelle à temps.
Il ne vous reste donc plus qu'à combattre. La créature est
invulnérable à la Discipline Kaï de la Puissance Psychique.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("VER DE PIERRE", 15, 38)], psychic_immune=True)
    if outcome == "win":
        st.write_stream(stream_text("Si vous êtes vainqueur, rendez-vous au :"))
        st.page_link("tomes/tome4/page_321.py", label="321", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
