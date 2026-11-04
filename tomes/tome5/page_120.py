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

check_inventory(current_page_number=120, book=5)

fr_text = """
Le poignard fend l'air en sifflant et vient se planter au milieu de
votre poitrine. Le souffle coupé par la douleur fulgurante, vous
tentez de retirer la lame de votre chair mais, dans votre hâte, vos
mains se mettent à trembler. Tandis que vous trébuchez en
arrière, le Garde se précipite vers vous, son visage hideux
parcouru par un sourire de triomphe. Finalement, vous parvenez
à retirer la lame et vous levez le poignard au-dessus de votre tête
en le pointant vers le Garde ; celui-ci voit le danger et plonge sur
vous, mais il est déjà trop tard : la lame lui a transpercé le cœur.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome5/page_22.py", label="22", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
