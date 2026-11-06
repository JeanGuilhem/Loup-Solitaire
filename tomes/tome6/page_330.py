import streamlit as st
from inventory import (
    can_shoot,
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

check_inventory(current_page_number=330, book=6)

fr_text = """
Vous redescendez le sentier et arrivez au croisement avec la
grand-route. Des cavaliers surgissent alors en file indienne de
derrière une maison en ruine. Ils s'avancent jusqu'au milieu du
village, où ils s'arrêtent brusquement. D'où vous êtes, vous ne
pouvez entendre leurs propos, mais vous comprenez à leurs
gestes saccadés qu'ils sont en train de se disputer. Ils repartent
bientôt et se dirigent dans votre direction avec Cyrilus, toujours
inconscient et ligoté sur la croupe du cheval du dernier cavalier.
Vous piquez des deux et disparaissez sous l'épais feuillage des
arbres qui bordent la route.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous possédez un Arc et que vous voulez leur tendre une embuscade lorsqu'ils passeront devant votre cachette, rendez-vous au :"))
    if can_shoot():
        st.page_link("tomes/tome6/page_20.py", label="20", icon="📄")
    else:
        st.page_link("tomes/tome6/page_20.py", label="20", icon="📄", disabled=True)

    st.write_stream(stream_text('Si vous préférez vous attaquer uniquement au dernier de la troupe afin de libérer Cyrilus, rendez-vous au :'))
    st.page_link("tomes/tome6/page_203.py", label="203", icon="📄")

    st.write_stream(stream_text('Si enfin vous préférez les laisser passer et les suivre à distance, rendez-vous au :'))
    st.page_link("tomes/tome6/page_227.py", label="227", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
