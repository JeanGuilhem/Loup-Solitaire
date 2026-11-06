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

check_inventory(current_page_number=196, book=6)

fr_text = """
Au bout de quelques minutes, vous voyez surgir la colonne de
cavaliers. Ils chevauchent en file indienne et vous reconnaissez
Cyrilus qui a perdu connaissance, solidement ligoté sur le dernier
cheval.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous possédez un Arc et que vous vouliez leur tendre une embuscade au moment où ils passeront devant votre cachette, rendez-vous au :"))
    st.page_link("tomes/tome6/page_20.py", label="20", icon="📄", disabled=not can_shoot())

    st.write_stream(stream_text("Si vous souhaitez attaquer uniquement le dernier cheval pour essayer de libérer Cyrilus, rendez-vous au :"))
    st.page_link("tomes/tome6/page_203.py", label="203", icon="📄")

    st.write_stream(stream_text("Enfin, si vous préférez les laisser passer puis les suivre à distance, rendez-vous au :"))
    st.page_link("tomes/tome6/page_227.py", label="227", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
