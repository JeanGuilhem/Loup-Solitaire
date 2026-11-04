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

check_inventory(current_page_number=205, book=5)

fr_text = """
Le vent qui siffle à vos oreilles colporte les hurlements
d'allégresse des Drakkars qui vous regardent aller à une mort
certaine.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre."))
    number = hazard_roll()
    if number is not None and number <= 4:
        st.write_stream(stream_text("Si le chiffre que vous avez tiré est compris entre 0 et 4, rendez-vous au :"))
        st.page_link("tomes/tome5/page_234.py", label="234", icon="📄")
    elif number is not None:
        st.write_stream(stream_text("Si le chiffre que vous avez tiré est compris entre 5 et 9, rendez-vous au :"))
        st.page_link("tomes/tome5/page_293.py", label="293", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
