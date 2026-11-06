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

check_inventory(current_page_number=215, book=6)

fr_text = """
Le pirate tombe raide mort à vos pieds. Aussitôt, trois de ses
camarades se ruent sur vous en poussant des cris rauques pour le
venger.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("PIRATES DES RIVIÈRES", 19, 28)], flee_after=2)
    if outcome == "fled":
        st.write_stream(stream_text("Si vous souhaitez cesser le combat après 2 Assauts, rendez-vous au :"))
        st.page_link("tomes/tome6/page_286.py", label="286", icon="📄")
    elif outcome == "win":
        st.write_stream(stream_text("Si vous l'emportez, rendez-vous au :"))
        st.page_link("tomes/tome6/page_111.py", label="111", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
