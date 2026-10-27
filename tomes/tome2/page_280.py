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

check_inventory(current_page_number=280, book=2)

fr_text = """
Vous dormez profondément jusqu'à l'aube sans être dérangé. A votre
réveil, vous ramassez vos affaires et vous allez rejoindre les autres à
bord de la diligence. Pendant deux jours, la diligence file sur la route
qui traverse les étendues plates et désolées du Pays Sauvage, en ne
faisant halte, de temps à autre, que pour permettre au cocher de prendre
quelque repos. Vous êtes arrivé au matin du 9e jour de votre quête
lorsqu'un malheureux accident se produit.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Utilisez la Table de Hasard pour obtenir un chiffre. Si vous tirez un chiffre entre 0 et 4, rendez-vous au 2. Entre 5 et 9, rendez-vous au 108.'))
    number = hazard_roll()
    if number is not None and number <= 4:
        st.page_link("tomes/tome2/page_2.py", label="2", icon="📄")
    elif number is not None:
        st.page_link("tomes/tome2/page_108.py", label="108", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
