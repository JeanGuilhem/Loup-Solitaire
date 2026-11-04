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

check_inventory(current_page_number=217, book=5)

fr_text = """
L'Itikar vous fixe d'un œil noir et froid, mais sans hostilité. Au
moment où vous vous installez sur la large selle, vous apercevez
les Drakkars se ruant sur la passerelle. Vous dénouez alors
rapidement la longue laisse qui retenait l'oiseau attaché, puis
vous empoignez les lourdes rênes de cuir.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome5/page_343.py", label="343", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
