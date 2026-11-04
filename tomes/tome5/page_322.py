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

check_inventory(current_page_number=322, book=5)

fr_text = """
L'escalier est haut et abrupt. Vous êtes à bout de souffle mais
vous continuez néanmoins à grimper sans faiblir, car les
Drakkars ne sont qu'à une douzaine de marches derrière vous.
En haut de la tour, un grand porche s'ouvre sur une plate-forme
où se trouve un énorme tambour. Celui-ci sert au gardien de la
tour pour envoyer des messages aux autres tours du Palais. Une
peau tannée a été tendue sur la surface de l'instrument et un
bâton en bois noir est accroché sur le côté.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez faire basculer le tambour et le précipiter dans l'escalier, rendez-vous au :"))
    st.page_link("tomes/tome5/page_329.py", label="329", icon="📄")

    st.write_stream(stream_text("Si vous préférez ne pas vous soucier de l'instrument et vous enfuir par la plate-forme, rendez-vous au :"))
    st.page_link("tomes/tome5/page_387.py", label="387", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
