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

check_inventory(current_page_number=198, book=6)

fr_text = """
Vous ne pouvez tirer qu'une seule fois avant que le monstre soit
sur vous. La moindre erreur vous serait fatale ! Pour arrêter net
la créature, vous devez atteindre un organe vital mais, dans la
pénombre de la chapelle en ruine, il vous est difficile de
distinguer clairement votre cible.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez viser la créature aux yeux, rendez-vous au :"))
    st.page_link("tomes/tome6/page_268.py", label="268", icon="📄")

    st.write_stream(stream_text("Si vous souhaitez la viser au cœur, rendez-vous au :"))
    st.page_link("tomes/tome6/page_243.py", label="243", icon="📄")

    st.write_stream(stream_text("Enfin, si vous préférez la viser aux jambes, rendez-vous au :"))
    st.page_link("tomes/tome6/page_95.py", label="95", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
