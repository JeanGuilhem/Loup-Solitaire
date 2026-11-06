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

check_inventory(current_page_number=93, book=6)

fr_text = """
Posant la main sur l'épaule de l'homme, vous le secouez
vigoureusement pour le tirer de sa torpeur éthylique, mais il
tombe de son tabouret et s'écroule par terre comme une masse.
C'est alors que vous découvrez une large tache de sang en plein
milieu de son dos, s'étalant autour d'un poignard planté jusqu'à
la garde. Tandis que vous reculez, saisi d'horreur, vous
entendez un faible cri au-dehors. C'est Cyrilus, il est sûrement
en difficulté !
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_317.py", label="317", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
