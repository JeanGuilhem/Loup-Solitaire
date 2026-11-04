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

check_inventory(current_page_number=12, book=5)

fr_text = """
Vous combattez sous l'eau avec un redoutable vampire des mers.
Déduisez 2 points de votre total d'HABILETÉ en raison de la
rapidité de l'attaque. Notez que la créature est insensible à la
Puissance Psychique.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("SANGSUE GÉANTE", 17, 11)], hability_modifier=-2, psychic_immune=True)
    if outcome == "win":
        st.write_stream(stream_text("Si vous sortez vainqueur de l'affrontement, rendez-vous au :"))
        st.page_link("tomes/tome5/page_95.py", label="95", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
