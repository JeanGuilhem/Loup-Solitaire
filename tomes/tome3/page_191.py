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

check_inventory(current_page_number=191, book=3)

fr_text = """
Tremblant de fatigue, vous parvenez enfin au fond du défilé alors
que la nuit tombe. Un peu plus loin, vous apercevez une grotte
située sous une chute d'eau gelée. Le vent souffle beaucoup plus
fort à présent et vous décidez de vous abriter dans cette grotte.
Lorsque vous y pénétrez, vous êtes surpris de distinguer, dans la
paroi du fond, un rayon de lumière qui filtre à travers une
fissure. Vous vous approchez prudemment de cette étrange lueur
mais hélas ! vous ne remarquez pas une crevasse dissimulée par
une couche de neige et vous y tombez dans une avalanche de
glace brisée.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome3/page_40.py", label="40", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
