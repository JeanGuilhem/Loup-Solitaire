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

check_inventory(current_page_number=208, book=4)

fr_text = """
Vous parcourez une vingtaine de mètres en courant et vous
arrivez soudain devant une paroi verticale. Ce souterrain n'a été
creusé que récemment et vous êtes dans un cul-de-sac.
Entendant le bruit des pas de vos poursuivants, vous faites
aussitôt volte-face. Votre seule chance de survie, désormais,
consiste à combattre les Gardes pour essayer de vous enfuir de ce
piège. Vous retournerez ensuite au croisement et vous prendrez
le tunnel de gauche. Mais vous n'aurez le droit de poursuivre
votre chemin qu'après avoir tué vos trois adversaires.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("Premier GARDE DES TUNNELS", 25, 24), ("2e GARDE", 22, 15), ("3e GARDE", 15, 14)])
    if outcome == "win":
        st.write_stream(stream_text('Si vous remportez la victoire, rendez-vous au :'))
        st.page_link("tomes/tome4/page_199.py", label="199", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
