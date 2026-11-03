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

check_inventory(current_page_number=106, book=4)

fr_text = """
Ces petits chevaux trapus appartiennent à une race connue sous
le nom de Kucheks. Ils ont été baptisés ainsi d'après le nom d'une
ville et d'une province situées en Vassagonie, à plusieurs
centaines de kilomètres à l'est. Les brigands que vous avez
rencontrés sur la voie de Ruanon chevauchaient précisément des
Kucheks.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez quitter Eshnar le plus vite possible, rendez-vous au :'))
    st.page_link("tomes/tome4/page_67.py", label="67", icon="📄")

    st.write_stream(stream_text('Si vous préférez fouiller les écuries, rendez-vous au :'))
    st.page_link("tomes/tome4/page_236.py", label="236", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
