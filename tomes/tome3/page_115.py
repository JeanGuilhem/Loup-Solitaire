import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=115, book=3)

fr_text = """
Vous vous apercevez qu'un grand nombre de ces os répandus
parmi les stalagmites ont appartenu à des squelettes humains.
Des crânes fracassés, des phalanges, des morceaux de thorax
sont ainsi à demi ensevelis dans la glace. Vous êtes sur le point
d'abandonner vos investigations lorsqu'une petite boîte en os
gravé attire votre attention.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez ouvrir cette boîte, rendez-vous au :"))
    st.page_link("tomes/tome3/page_218.py", label="218", icon="📄")
    st.write_stream(stream_text("Si vous préférez ne pas y toucher, vous pouvez à présent examiner la porte de la forteresse en vous rendant au :"))
    st.page_link("tomes/tome3/page_52.py", label="52", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
