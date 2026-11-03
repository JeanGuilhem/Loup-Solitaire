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

check_inventory(current_page_number=89, book=4)

fr_text = """
Vous vous frayez un chemin en portant des coups de tous côtés
aux bandits qui vous encerclent, guidant votre cheval par la
simple pression de vos genoux. Vous apercevez un peu plus loin
une éminence de terre boueuse vers laquelle vous vous précipitez
dans l'espoir de pouvoir rassembler vos hommes. Vous
approchez du sommet de l'éminence lorsqu'un Guerrier vêtu
d'une armure vous attaque par le flanc, sa lance pointée vers
votre gorge. Il vous est impossible de fuir, vous devrez le
combattre jusqu'à la mort de l'un de vous deux.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("GUERRIER PILLARD", 17, 26)])
    if outcome == "win":
        st.write_stream(stream_text("Si vous êtes vainqueur, rendez-vous au :"))
        st.page_link("tomes/tome4/page_7.py", label="7", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
