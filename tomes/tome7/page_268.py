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

check_inventory(current_page_number=268, book=7)

fr_text = """
Vous sautez ensemble par-dessus la dalle et vous vous recevez
sur le sol ferme, de l'autre côté, en effectuant un roulé-boulé. Les
créatures lèvent leurs bras sinueux en riant cruellement et font
jaillir à l'extrémité de leurs doigts palmés de longues griffes
recourbées ressemblant à des couteaux d'assassin. Elles se
précipitent en avant pour vous attaquer mais, aveuglées par leur
soif de sang, elles ne voient pas le danger qui se trouve sous leurs
sabots fourchus. En un instant, leurs jacassements se
transforment en lamentations tandis que la dalle se dérobe sous
leurs sabots. Les créatures tombent comme des pierres et
disparaissent dans le gouffre noir et profond en hurlant.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome7/page_12.py", label="12", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
