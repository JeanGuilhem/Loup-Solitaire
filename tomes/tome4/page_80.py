import streamlit as st
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

check_inventory(current_page_number=80, book=4)

fr_text = """
Bien que le feu ait complètement détruit tout signe distinctif qui
aurait pu l'identifier, vous parvenez à reconnaître dans ces débris
calcinés un chariot militaire ayant appartenu à la cavalerie du
Sommerlund. C'est l'un des trois véhicules que le capitaine Gayal
et ses hommes escortaient au moment de leur disparition. Ce
chariot transportait des vivres et du matériel à son départ de
Holmgard, il y a un mois, mais il ne reste plus de son chargement
que des tas de cendres. Après vous être assuré qu'aucun indice
pouvant vous renseigner sur le sort du capitaine Gayal ne vous a
échappé, vous remontez en selle et vous menez vos hommes en
direction du sud le long de la grand-route.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome4/page_175.py", label="175", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
