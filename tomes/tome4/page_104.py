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

check_inventory(current_page_number=104, book=4)

fr_text = """
Rassemblant toutes vos ressources musculaires et nerveuses,
vous vous précipitez de l'autre côté du pont. Le sang vous bat aux
oreilles et vous faites des prières pour que les broches de fixation
tiennent encore quelques instants. Vous êtes à peine à 3 mètres
du but lorsque le pont se détache soudain.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous voulez vous accrocher aux planches du pont, rendez-vous au :'))
    st.page_link("tomes/tome4/page_303.py", label="303", icon="📄")

    st.write_stream(stream_text('Si vous préférez sauter du pont et vous laisser tomber dans les profondeurs inconnues du puits de mine, rendez-vous au :'))
    st.page_link("tomes/tome4/page_342.py", label="342", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
