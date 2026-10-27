import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import stream_text, called_cookies, hazard_roll

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=278, book=2)

fr_text = """
Vous agitez désespérément votre cape au-dessus de vous jusqu'à ce que
vous soyez au bord de l'épuisement.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Utilisez la Table de Hasard pour obtenir un chiffre qui vous indiquera si vos efforts ont été couronnés de succès. Si vous tirez un chiffre entre 0 et 6, rendez-vous au 41. Si vous obtenez 7, 8 ou 9, rendez-vous au 180.'))
    number = hazard_roll()
    if number is not None and number <= 6:
        st.page_link("tomes/tome2/page_41.py", label="41", icon="📄")
    elif number is not None:
        st.page_link("tomes/tome2/page_180.py", label="180", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
