import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=180, book=2)

fr_text = """
Vous arrivez à la conclusion que les marins du bateau sont aveugles ou
qu'ils n'ont pas la moindre intention de vous porter secours. En effet, le
bateau de pêche poursuit sa course et disparaît bientôt à l'horizon sans
s'occuper de vous. En désespoir de cause, vous arrachez une planche du
panneau d'écoutille et vous vous en servez comme d'une rame pour
pagayer en direction de la côte.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_337.py", label="337", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
