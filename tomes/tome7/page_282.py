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

check_inventory(current_page_number=282, book=7)

fr_text = """
Vous entendez des bruits de pas dans l'escalier : d'autres
ennemis approchent. S'ils ont, eux aussi, des arbalètes, vos
chances de survie seront alors très minces. Devant vous se dresse
une grande porte en bronze à double battant, et vous apercevez,
de chaque côté, des tapisseries et des statuettes en or.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez ouvrir les battants, rendez-vous au :"))
    st.page_link("tomes/tome7/page_159.py", label="159", icon="📄")

    st.write_stream(stream_text("Si vous voulez examiner les tapisseries, rendez-vous au :"))
    st.page_link("tomes/tome7/page_74.py", label="74", icon="📄")

    st.write_stream(stream_text("Si vous préférez vous préparer à affronter l'ennemi qui approche, rendez-vous au :"))
    st.page_link("tomes/tome7/page_273.py", label="273", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
