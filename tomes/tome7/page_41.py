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

check_inventory(current_page_number=41, book=7)

fr_text = """
Vous êtes poursuivi par un terrible grondement tandis que vous
courez sur le lugubre rivage, en direction de la haute paroi
rocheuse qui sert de fondation à Kazan-Oud. Tout d'abord, vous
trouvez le sable agréablement chaud mais, au bout de quelques
minutes, vous sentez les semelles de vos bottes devenir brûlantes
! A quelques mètres devant vous, vous apercevez un alignement
de pierres qui part du sable noir jusqu'à une fissure irrégulière
s'ouvrant dans la paroi rocheuse.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous voulez sauter sur la première pierre, rendez-vous au :'))
    st.page_link("tomes/tome7/page_177.py", label="177", icon="📄")

    st.write_stream(stream_text('Si vous préférez éviter ces dalles et continuer à avancer, tant bien que mal, sur le sable brûlant, rendez-vous au :'))
    st.page_link("tomes/tome7/page_104.py", label="104", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
