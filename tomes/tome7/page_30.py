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

check_inventory(current_page_number=30, book=7)

fr_text = """
Curieusement, le sable est chaud et, au fur et à mesure que vous
avancez entre les blocs de rocher qui jonchent la plage, la semelle
de vos bottes devient de plus en plus brûlante. A quelques mètres
de vous, vous apercevez un alignement de pierres qui mène
jusqu'à une fissure s'ouvrant dans la paroi rocheuse.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous voulez sauter sur la première pierre, rendez-vous au :'))
    st.page_link("tomes/tome7/page_177.py", label="177", icon="📄")

    st.write_stream(stream_text('Si vous préférez éviter ces dalles et continuer, tant bien que mal, à marcher sur le sable brûlant, rendez-vous au :'))
    st.page_link("tomes/tome7/page_104.py", label="104", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
