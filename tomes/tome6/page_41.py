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

check_inventory(current_page_number=41, book=6)

fr_text = """
Vous pressentez que la voie de gauche recèle une force hostile et
dangereuse. Vous n'arrivez pas à savoir quoi exactement, mais
l'aura de malfaisance et de vilenie qui en émane est extrêmement
forte.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez démasquer l'horreur qui se tapit dans la ruelle de gauche, rendez-vous au :"))
    st.page_link("tomes/tome6/page_151.py", label="151", icon="📄")

    st.write_stream(stream_text("Si vous jugez plus prudent d'éviter toute rencontre avec cette présence maléfique, prenez la voie de droite et rendez-vous au :"))
    st.page_link("tomes/tome6/page_289.py", label="289", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
