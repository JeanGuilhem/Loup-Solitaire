import streamlit as st
from inventory import (
    add_to_inventory,
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    is_new_page,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=142, book=2)

fr_text = """
L'homme prend votre argent et vous tend un laissez-passer valable sept
jours. Vous le remerciez puis vous quittez les lieux. Au-dehors, vous
prenez à gauche et vous vous approchez des gardes qui se tiennent en
faction au bout de la rue.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page() and not has_item("LAISSEZ-PASSER BLANC"):
        add_to_inventory("LAISSEZ-PASSER BLANC")
    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_246.py", label="246", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
