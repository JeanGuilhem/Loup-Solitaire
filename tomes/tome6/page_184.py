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

check_inventory(current_page_number=184, book=6)

fr_text = """
Le poignard vous arrache une touffe de cheveux avant de
s'enfoncer profondément dans le bois du bastingage. La rapidité
de votre esquive a complètement désorienté le pirate qui perd
l'équilibre. Vous vous relevez rapidement et vous passez à
l'attaque. Sans même savoir ce qui vient de le frapper, il bascule
par-dessus bord et tombe dans les eaux froides et profondes de la
Storn.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_254.py", label="254", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
