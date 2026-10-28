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

check_inventory(current_page_number=256, book=3)

fr_text = """
La porte claque dans votre dos, vous interdisant désormais de
revenir dans le couloir. Peu à peu, vous sentez le sol vibrer, mais
cette trépidation n'est que de courte durée : dès qu'elle a cessé,
vous entendez un faible déclic et vous voyez aussitôt une fissure
apparaître sur le monolithe noir. La fissure est visible tout autour
du bloc de pierre et elle s'élargit de plus en plus.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez vous préparer au combat, rendez-vous au :'))
    st.page_link("tomes/tome3/page_217.py", label="217", icon="📄")

    st.write_stream(stream_text('Si vous préférez vous abriter dans un coin en vous couvrant de votre cape, rendez-vous au :'))
    st.page_link("tomes/tome3/page_7.py", label="7", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
