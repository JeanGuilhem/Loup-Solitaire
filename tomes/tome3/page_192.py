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

fr_unknown_item = "Vous ne possédez pas cet objet."

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=192, book=3)

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write_stream(stream_text('Si vous possédez une Pierre Rayonnante, rendez-vous au :'))
    if has_item("PIERRE RAYONNANTE"):
        st.page_link("tomes/tome3/page_267.py", label="267", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome3/page_267.py", label="267", icon="📄", disabled=True)
    st.write_stream(stream_text('Sinon, rendez-vous au :'))
    st.page_link("tomes/tome3/page_44.py", label="44", icon="📄", disabled=has_item("PIERRE RAYONNANTE"))

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
