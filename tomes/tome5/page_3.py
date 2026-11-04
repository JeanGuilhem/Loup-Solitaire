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

check_inventory(current_page_number=3, book=5)

fr_text = """
En fouillant le cadavre des trois Gardes du vestibule, vous
découvrez les objets suivants : 4 Pièces d'Or, une Épée, un
Poignard, une Potion d'Alether (qui vous fera gagner 2 points
d'HABILETÉ lors d'un combat). Si vous le désirez, vous pouvez
également prendre la Sarbacane et la Flèche de Sommeil qui
restent. Dans ce cas, n'oubliez pas de les inscrire sur votre Feuille
d'Aventure dans la case Sac à Dos. Dans les vêtements du
guerrier à la sarbacane, vous trouvez également un fragment de
parchemin sur lequel sont inscrits la date de ce jour et le chiffre
67. Un sourire éclaire votre visage lorsque vous réalisez qu'il
s'agit du chiffre qui commande l'ouverture de la porte de bronze !
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    pickup_gold(4, key="gold")
    pickup_button("ÉPÉE", key="epee", label="Prendre l'Épée")
    pickup_button("POIGNARD", key="poignard", label="Prendre le Poignard")
    pickup_button("FIOLE D'ALÉTHER", key="alether", label="Prendre la Potion d'Alether")
    pickup_button("SARBACANE", key="sarbacane", label="Prendre la Sarbacane")
    pickup_button("FLÈCHE DE SOMMEIL", key="fleche", label="Prendre la Flèche de Sommeil")

    st.write_stream(stream_text('Retenant votre souffle, vous composez le numéro. Rendez-vous au :'))
    st.page_link("tomes/tome5/page_67.py", label="67", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
