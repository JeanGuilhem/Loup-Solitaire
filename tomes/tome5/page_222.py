import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=222, book=5)

fr_text = """
Vous devez agir rapidement, si vous voulez éviter d'être repéré,
car la créature rouge est un Vordak, un des puissants morts
vivants qui sont au service des Seigneurs des Ténèbres.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre."))
    number = hazard_roll()
    if number is not None and number <= 2:
        st.write_stream(stream_text("Si vous avez tiré 0, 1 ou 2, rendez-vous au :"))
        st.page_link("tomes/tome5/page_378.py", label="378", icon="📄")
    elif number is not None:
        st.write_stream(stream_text("Si vous avez tiré un chiffre entre 3 et 9, rendez-vous au :"))
        st.page_link("tomes/tome5/page_262.py", label="262", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
