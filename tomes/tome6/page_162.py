import streamlit as st
from inventory import (
    can_shoot,
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

check_inventory(current_page_number=162, book=6)

fr_text = """
Mû par l'instinct, vous plongez à terre, roulez sur le côté, puis
tirez votre arme en vous remettant debout d'un bond agile. Cet
extraordinaire réflexe vient de vous sauver des griffes d'un
énorme monstre à la gueule aplatie, qui s'attaque aux pèlerins
venus sans méfiance s'abreuver à la source. Cependant,
l'abominable créature ne s'avoue pas vaincue : les yeux luisant de
cruauté, elle se précipite sur vous avec voracité, en poussant un
horrible grognement.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous possédez un Arc, rendez-vous au :"))
    st.page_link("tomes/tome6/page_198.py", label="198", icon="📄", disabled=not can_shoot())

    st.write_stream(stream_text("Si vous n'en avez pas, rendez-vous au :"))
    st.page_link("tomes/tome6/page_343.py", label="343", icon="📄", disabled=can_shoot())

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
