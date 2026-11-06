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

check_inventory(current_page_number=92, book=6)

fr_text = """
L'homme pousse son cri de guerre et se rue sur vous en
brandissant un redoutable sabre d'abordage.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("PIRATE DES RIVIÈRES", 17, 23)], flee_after=0)
    if outcome == "fled":
        st.write_stream(stream_text("Vous cessez le combat : rendez-vous au :"))
        st.page_link("tomes/tome6/page_286.py", label="286", icon="📄")
    if outcome == "win":
        if st.session_state["combat_combat"]["round"] <= 3:
            st.write_stream(stream_text("Vous sortez vainqueur de l'affrontement en 3 Assauts ou moins : rendez-vous au :"))
            st.page_link("tomes/tome6/page_77.py", label="77", icon="📄")
        else:
            st.write_stream(stream_text("Le combat s'est prolongé au-delà de 3 Assauts : rendez-vous au :"))
            st.page_link("tomes/tome6/page_215.py", label="215", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
