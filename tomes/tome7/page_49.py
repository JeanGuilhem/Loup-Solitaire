import streamlit as st
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

check_inventory(current_page_number=49, book=7)

fr_text = """
Une fois la lumière faite, vous remarquez que le sol inégal est
jonché de débris couverts de moisissure et aspergés de sang
séché. Vous vous apprêtez à inspecter un étroit tunnel qui part en
serpentant sous le noir rocher, lorsque votre instinct de Maître
Kaï vous prévient qu'il y a, juste devant vous, une marche pas
très haute allant d'un côté à l'autre de la grotte. En l'examinant
de plus près, vous constatez qu'il s'agit d'une grande dalle de
marbre recouvrant les trois premiers mètres du tunnel.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez examiner cette dalle de marbre de la pointe de votre arme, afin de savoir s'il y a un piège, rendez-vous au :"))
    st.page_link("tomes/tome7/page_183.py", label="183", icon="📄")

    st.write_stream(stream_text('Si vous désirez sauter par-dessus la dalle et continuer au-delà, rendez-vous au :'))
    st.page_link("tomes/tome7/page_127.py", label="127", icon="📄")

    st.write_stream(stream_text('Si vous êtes décidé à entrer dans le tunnel en marchant carrément sur la dalle, rendez-vous au :'))
    st.page_link("tomes/tome7/page_277.py", label="277", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
