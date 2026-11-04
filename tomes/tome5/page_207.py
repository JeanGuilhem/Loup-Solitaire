import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    pickup_button,
    pickup_gold,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=207, book=5)

fr_text = """
Vos découvertes ne présentent que peu d'intérêt : 8 Pièces d'Or
et 1 Sifflet de Cuivre attaché à une chaîne que le Garde porte
autour du cou. Vous pouvez prendre ces objets si vous le désirez,
mais n'oubliez pas de les noter sur votre Feuille d'Aventure.
Soudain, des bruits de pas vous signalent l'arrivée d'individus
peu désirables : des Drakkars ! Ceux-ci se pressent sur le sentier
pavé qui mène aux enclos. Sans hésiter une seule seconde, vous
pénétrez dans l'enclos de l'Itikar.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    pickup_gold(8, key="or_garde")
    pickup_button("SIFFLET DE CUIVRE", key="sifflet", label="Prendre le Sifflet de Cuivre")

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome5/page_224.py", label="224", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
