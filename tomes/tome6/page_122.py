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

check_inventory(current_page_number=122, book=6)

fr_text = """
Votre instinct vous avertit qu'un terrible précipice s'ouvre à
pic derrière la brèche du rempart. Continuer dans cette
direction pourrait bien vous être fatal !
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous désirez, malgré tout, ignorer le danger et escalader le mur pour passer par la brèche, rendez-vous au :"))
    st.page_link("tomes/tome6/page_217.py", label="217", icon="📄")

    st.write_stream(stream_text("Si vous jugez plus prudent de dévaler l'escalier en direction de la porte de fer, rendez-vous au :"))
    st.page_link("tomes/tome6/page_169.py", label="169", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
