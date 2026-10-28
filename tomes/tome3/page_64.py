import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=64, book=3)

fr_text = """
Vous avez le sentiment désagréable qu'un danger vous guette
dans l'un et l'autre tunnels. Le tunnel orienté au nord est le plus
dangereux, vous le sentez, mais vous êtes également convaincu
que c'est le plus court chemin pour gagner Ikaya.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez entrer dans le tunnel nord, rendez-vous au :'))
    st.page_link("tomes/tome3/page_235.py", label="235", icon="📄")

    st.write_stream(stream_text('Si vous préférez le tunnel ouest, rendez-vous au :'))
    st.page_link("tomes/tome3/page_275.py", label="275", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
