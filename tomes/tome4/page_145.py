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

check_inventory(current_page_number=145, book=4)

fr_text = """
Le tunnel descend sur des kilomètres, s'enfonçant dans la roche.
De temps à autre, vous sursautez en voyant surgir des essaims de
mouches luisantes ou des chauves-souris qui volettent autour de
vous dans l'obscurité, attirées par la chaleur de votre corps. Vous
atteignez enfin une salle dans laquelle une petite cabane de bois a
été construite contre le mur. Vous êtes épuisé et quelques heures
de sommeil vous seraient nécessaires.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez entrer dans la cabane pour vous y reposer, rendez-vous au :'))
    st.page_link("tomes/tome4/page_322.py", label="322", icon="📄")

    st.write_stream(stream_text('Si vous préférez poursuivre votre chemin en ignorant votre fatigue, rendez-vous au :'))
    st.page_link("tomes/tome4/page_162.py", label="162", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
