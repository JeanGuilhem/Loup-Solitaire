import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies, hazard_roll

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=179, book=3)

fr_text = """
Vous imaginez un plan particulièrement audacieux. En vous
faisant passer pour un Barbare des Glaces, vous pourriez en effet
poser le bol près des gardes ; dans la pénombre du couloir, il leur
serait difficile d'apercevoir la fumée. Loi-Kymar approuve votre
plan et prépare un mélange d'herbes destiné à vous protéger
vous-même contre les vapeurs nocives. Vêtu des fourrures d'un
Barbare des Glaces, vous avancez bientôt dans le couloir, le bol
caché sous vos vêtements.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Utilisez la Table de Hasard pour obtenir un chiffre.'))
    roll = hazard_roll()
    if roll is not None and roll <= 4:
        st.write_stream(stream_text('Si vous tirez un chiffre entre 0 et 4, rendez-vous au :'))
        st.page_link("tomes/tome3/page_39.py", label="39", icon="📄")
    elif roll is not None:
        st.write_stream(stream_text('Entre 5 et 9, rendez-vous au :'))
        st.page_link("tomes/tome3/page_296.py", label="296", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
