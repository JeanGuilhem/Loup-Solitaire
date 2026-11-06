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

check_inventory(current_page_number=28, book=6)

fr_text = """
Alors que le guerrier s'écrase à terre, vous remarquez que votre
compagnon de route est aux prises avec cinq cavaliers armés
jusqu'aux dents. Cyrilus est encerclé et ses chances d'en sortir
sont plus que minces. Soudain, l'un des hommes lui assène un
violent coup de masse sur la nuque, anéantissant ainsi toute
tentative de résistance de sa part. Votre infortuné compagnon
s'affale mollement sur l'encolure de son cheval et les cavaliers,
prenant celui-ci par la bride, emportent leur captif et traversent
le pont au triple galop.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez vous lancer à leur poursuite, rendez-vous au :"))
    st.page_link("tomes/tome6/page_39.py", label="39", icon="📄")

    st.write_stream(stream_text("Si vous préférez fouiller la dépouille de votre adversaire, rendez-vous au :"))
    st.page_link("tomes/tome6/page_139.py", label="139", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
