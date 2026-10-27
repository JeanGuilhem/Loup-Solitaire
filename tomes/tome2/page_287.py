import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=287, book=2)

fr_text = """
Vous concentrez toute votre énergie de Seigneur Kaï sur la petite
serrure de cuivre et, quelques instants plus tard, un déclic à l'intérieur
du coffret vous indique que le pêne vient de sortir de sa gâche ; vous
soulevez alors le couvercle de la boîte et vous y découvrez un
parchemin frappé du Sceau Royal du Sommerlund. Le document
contient des instructions confidentielles concernant votre mission. En
remettant ensuite le coffret à sa place, vous vous apercevez qu'un
mécanisme secret a été aménagé dans le couvercle pour faire échec aux
espions : sans le secours de votre Discipline Kaï, une aiguille
empoisonnée aurait jailli de la boîte et se serait enfoncée dans votre
épiderme, provoquant une mort instantanée. Vous refermez les tiroirs et
vous prenez bien soin d'effacer toute trace de votre fouille avant d'aller
rejoindre le capitaine sur le pont du navire.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome2/page_175.py", label="175", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
