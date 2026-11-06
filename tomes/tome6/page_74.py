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

check_inventory(current_page_number=74, book=6)

fr_text = """
Il ne se passe pas longtemps avant que les cavaliers
réapparaissent. Vous croyant parti au loin, ils émergent en file
indienne de derrière une petite masure délabrée, puis ils
forment un cercle au milieu du village. Bien que vous ne
puissiez pas entendre ce qu'ils disent, vous devinez à leurs
gestes nerveux qu'ils tiennent une discussion animée. Peu après,
ils rompent le cercle et partent au petit trot dans votre
direction. Cyrilus, toujours inconscient, gît en travers de son
cheval et est remorqué par le dernier cavalier.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous possédez un Arc et si vous voulez tendre une embuscade à la horde au moment où elle passera inévitablement devant vous, rendez-vous au :"))
    st.page_link("tomes/tome6/page_20.py", label="20", icon="📄", disabled=not can_shoot())

    st.write_stream(stream_text("Si vous préférez attaquer le dernier cavalier pour tenter de délivrer Cyrilus, rendez-vous au :"))
    st.page_link("tomes/tome6/page_203.py", label="203", icon="📄")

    st.write_stream(stream_text("Si vous jugez plus prudent de les laisser passer et de les suivre discrètement, rendez-vous au :"))
    st.page_link("tomes/tome6/page_227.py", label="227", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
