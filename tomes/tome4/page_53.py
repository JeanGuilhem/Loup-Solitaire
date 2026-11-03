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

check_inventory(current_page_number=53, book=4)

fr_text = """
Dès que vous êtes entré, la porte se referme dans votre dos en
claquant. Vous faites aussitôt volte-face au moment où un Bandit
émergeant de l'ombre, se précipite sur vous. Il a la tête
enveloppée de pansements tachés de sang, ce qui ne l'empêche
pas d'être armé et bien décidé à vous combattre.

Il vous affronte le dos contre la porte et vous n'avez donc pas la
possibilité de fuir.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("BANDIT BLESSÉ", 13, 16)])
    if outcome == "win":
        st.write_stream(stream_text("Si vous remportez la victoire, rendez-vous au :"))
        st.page_link("tomes/tome4/page_109.py", label="109", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
