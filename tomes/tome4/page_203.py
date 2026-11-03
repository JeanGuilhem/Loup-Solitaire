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

check_inventory(current_page_number=203, book=4)

fr_text = """
Tandis que le Garde tombe mort à vos pieds, trois de vos
poursuivants font leur apparition. Ils sont vêtus de lourdes
armures et chacun d'eux est armé d'une hallebarde à l'aspect
particulièrement redoutable.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez engager le combat, rendez-vous au :'))
    st.page_link("tomes/tome4/page_108.py", label="108", icon="📄")

    st.write_stream(stream_text('Si vous préférez vous enfuir en franchissant le pont, rendez-vous au :'))
    st.page_link("tomes/tome4/page_271.py", label="271", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
