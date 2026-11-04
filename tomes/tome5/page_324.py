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

check_inventory(current_page_number=324, book=5)

fr_text = """
Vous n'êtes plus qu'à quelques mètres de la sentinelle lorsque
celle-ci sent soudain votre présence. Elle se retourne rapidement
et vous fait face au moment où vous passez à l'attaque.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("SENTINELLE DRAKKAR", 18, 25)])
    if outcome == "win":
        st.write_stream(stream_text("Si vous sortez vainqueur de l'affrontement, cachez le corps de votre victime avant d'entrer dans le Tombeau, puis rendez-vous au :"))
        st.page_link("tomes/tome5/page_395.py", label="395", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
