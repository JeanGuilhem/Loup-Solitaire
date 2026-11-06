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

check_inventory(current_page_number=331, book=6)

fr_text = """
Vous chevauchez toute la nuit sans dormir, éclairé par le seul
clair de lune, avec pour unique compagnon le vent qui hurle à
travers la plaine. Alors que les premières lumières de l'aube
pointent à l'horizon, vous apercevez un petit village à moins d'un
kilomètre devant vous sur la route. Au moment où vous allez
pénétrer dans le village, un petit chien hargneux surgit
brusquement et vous suit en mordillant les jarrets de votre
monture ; vous devez le repousser de la pointe de la botte. Vous
poursuivez votre avance à travers les rues jonchées d'ordures de
toutes sortes. A l'autre bout du village, là où la grand-route
disparaît entre deux rangées de mamelons dispersés, se dresse
un manoir fortifié. Sur une large pancarte délavée par la pluie,
vous parvenez à lire cette curieuse inscription :

**PASS POUR AMORY : 3 PIÈCES D'OR**
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez vous arrêter au manoir pour vous renseigner sur le sens de cette indication, rendez-vous au :'))
    st.page_link("tomes/tome6/page_27.py", label="27", icon="📄")

    st.write_stream(stream_text('Si vous préférez continuer directement vers Amory, rendez-vous au :'))
    st.page_link("tomes/tome6/page_146.py", label="146", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
