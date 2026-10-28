import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=50, book=3)

fr_unknown_item = "Vous ne possédez pas cet objet."

fr_text = """
Avez-vous découvert l'Ancien Temple d'Ikaya et emporté avec
vous une Pierre Rayonnante ?
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous possédez cet Objet Spécial, rendez-vous au :'))
    if has_item("PIERRE RAYONNANTE"):
        st.page_link("tomes/tome3/page_139.py", label="139", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome3/page_139.py", label="139", icon="📄", disabled=True)

    st.write_stream(stream_text('Dans le cas contraire, rendez-vous au :'))
    st.page_link("tomes/tome3/page_189.py", label="189", icon="📄", disabled=has_item("PIERRE RAYONNANTE"))

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
