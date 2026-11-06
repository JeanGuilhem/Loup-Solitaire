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

check_inventory(current_page_number=156, book=6)

fr_text = """
Seule une formidable poussée parviendra à casser la croûte de
poussière et de saleté accumulées depuis des années autour de la
porte.
"""

fr_text_2 = """
Pour ouvrir cette porte, suivez les règles habituelles de combat.
Les points d'ENDURANCE que vous perdez éventuellement
représentent la fatigue que vous endurez pour en venir à bout.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write(fr_text_2)

    # la porte est un adversaire « Résistance » : insensible aux pouvoirs psychiques ; abandon à tout moment
    outcome = combat([("PORTE DES ÉGOUTS", 13, 35)], psychic_immune=True, flee_after=0)
    if outcome == "fled":
        st.write_stream(stream_text("Vous interrompez vos efforts pour continuer à longer le tunnel ; rendez-vous au :"))
        st.page_link("tomes/tome6/page_339.py", label="339", icon="📄")
    elif outcome == "win":
        st.write_stream(stream_text("La porte cède à votre pression ; rendez-vous au :"))
        st.page_link("tomes/tome6/page_200.py", label="200", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
