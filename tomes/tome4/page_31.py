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

check_inventory(current_page_number=31, book=4)

fr_text = """
L'eau est sombre, très froide et son courant tumultueux vous
emporte irrésistiblement vers un nouveau danger que vous
n'aviez pas prévu : des rapides. Le fracas de l'eau bouillonnante
est si intense qu'il en devient assourdissant. Vous aspirez une
grande bouffée d'air en vous préparant à affronter les remous
torrentiels qui menacent de vous engloutir.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre. Si vous tirez un chiffre entre 0 et 4, rendez-vous au 272. Entre 5 et 9, rendez-vous au 329."))
    number = hazard_roll()
    if number is not None and number <= 4:
        st.page_link("tomes/tome4/page_272.py", label="272", icon="📄")
    elif number is not None:
        st.page_link("tomes/tome4/page_329.py", label="329", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
