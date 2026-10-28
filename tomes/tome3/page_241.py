import streamlit as st
from combat import combat
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=241, book=3)

fr_text = """
Le Barbare des Glaces n'a pas eu le temps de se relever lorsque
vous l'attaquez ; il est encore à genoux et incapable de réagir
pendant les deux premiers Assauts. En conséquence, vous ne
perdrez aucun point d'ENDURANCE au cours de ces deux
premiers Assauts, quelles que soient les indications données par
la Table des Coups Portés. Votre adversaire, en revanche, perdra
tous les points d'ENDURANCE indiqués par cette même Table.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("BARBARE DES GLACES", 18, 28)], ls_immune_rounds=2)
    if outcome == "win":
        st.write_stream(stream_text("Vous sortez vainqueur de cet affrontement, rendez-vous au :"))
        st.page_link("tomes/tome3/page_186.py", label="186", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
