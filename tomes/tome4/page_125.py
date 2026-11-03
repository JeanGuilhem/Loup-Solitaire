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

check_inventory(current_page_number=125, book=4)

fr_text = """
Vous esquissez un sourire en tirant sur la corde de toutes vos
forces puis vous vous tournez alors vers vos poursuivants en
étant convaincu qu'ils vont être précipités dans le puits de mine.
Malheureusement, ce n'est pas le pont qui s'abat, mais une
lourde herse qui bloque instantanément l'entrée du tunnel. Vos
ennemis éclatent d'un rire sardonique et dégainent leurs armes
en se lançant à l'attaque. Il vous est impossible de prendre la
fuite et il vous faut les combattre un par un à mesure qu'ils
franchissent le pont.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([
        ("CHEF DES GARDES", 20, 30),
        ("1er GARDE DES TUNNELS", 18, 26),
        ("2e GARDE DES TUNNELS", 16, 24),
    ])
    if outcome == "win":
        st.write_stream(stream_text('Si vous êtes vainqueur rendez-vous au :'))
        st.page_link("tomes/tome4/page_261.py", label="261", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
