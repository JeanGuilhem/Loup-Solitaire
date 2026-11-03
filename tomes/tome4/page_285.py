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

check_inventory(current_page_number=285, book=4)

fr_text = """
Vous vous précipitez en haut des marches pour attaquer les
Gardes. Ces derniers tirent aussitôt une volée de carreaux
d'arbalètes et l'une des flèches à la pointe de métal transperce le
capuchon de votre cape. Par miracle, vous n'êtes pas touché.
Vous levez alors votre arme et vous frappez, fracassant le crâne
du garde qui a tiré sur vous. A peine s'est-il effondré dans
l'escalier que l'un de ses compagnons s'avance pour vous
combattre. Il vous est impossible de vous enfuir et vous devrez
affronter ce nouvel adversaire jusqu'à la mort de l'un de vous
deux.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("GARDE", 16, 28)])
    if outcome == "win":
        st.write_stream(stream_text('Si vous remportez la victoire, rendez-vous au :'))
        st.page_link("tomes/tome4/page_71.py", label="71", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
