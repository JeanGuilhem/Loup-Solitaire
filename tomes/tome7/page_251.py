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

check_inventory(current_page_number=251, book=7)

fr_text = """
Grâce à votre Discipline Magnakaï, vous parvenez à distinguer
les contours d'un alignement de pierres menant jusqu'à une
étroite fissure dans la paroi rocheuse, et vous sentez qu'il y a une
entrée à cet endroit.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez descendre sur la plage pour examiner cette fissure, rendez-vous au :"))
    st.page_link("tomes/tome7/page_303.py", label="303", icon="📄")

    st.write_stream(stream_text("Si vous préférez monter les marches vers l'entrée de la grotte, rendez-vous au :"))
    st.page_link("tomes/tome7/page_82.py", label="82", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
