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

check_inventory(current_page_number=179, book=6)

fr_text = """
Ils refusent catégoriquement. « Nous ne laisserons personne
toucher à un des pontons car, expliquent-ils, si un seul vient à
disparaître, chacun d'entre nous recevra cent coups de fouet en
châtiment. » Ils vous surveillent d'un œil attentif jusqu'à ce que
vous ayez quitté le camp. Résigné, vous vous apprêtez à traverser
les eaux froides à la nage.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_171.py", label="171", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
