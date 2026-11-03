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

check_inventory(current_page_number=235, book=4)

fr_text = """
Le souterrain aboutit à un escalier qui s'enfonce à une trentaine
de mètres de profondeur. Au bas des marches, un petit couloir
mène à un croisement où vous découvrez un tunnel orienté nord-sud.
En direction du nord, vous apercevez une caverne éclairée
par des Torches. Des meurtrières sont aménagées dans ses
parois. Au sud, le tunnel aboutit à une sorte de balcon.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez explorer la caverne, rendez-vous au :'))
    st.page_link("tomes/tome4/page_177.py", label="177", icon="📄")

    st.write_stream(stream_text('Si vous préférez vous diriger vers le balcon, rendez-vous au :'))
    st.page_link("tomes/tome4/page_100.py", label="100", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
