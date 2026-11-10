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

check_inventory(current_page_number=136, book=7)

fr_text = """
L'attaque psychique cesse dès que vous frappez la main. Bien que
votre coup ne lui ait infligé aucune blessure apparente, la main
devient subitement flasque et s'écroule au bas de son socle.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez l'attaquer à nouveau, rendez-vous au :"))
    st.page_link("tomes/tome7/page_116.py", label="116", icon="📄")

    st.write_stream(stream_text("Si vous préférez ne plus vous en occuper et passer entre les deux piliers verts, afin de gagner le passage qui s'ouvre au-delà, rendez-vous au :"))
    st.page_link("tomes/tome7/page_103.py", label="103", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
