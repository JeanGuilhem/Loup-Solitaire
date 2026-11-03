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

check_inventory(current_page_number=187, book=4)

fr_text = """
En émergeant du tunnel sous le soleil du matin, vous vous
débarrassez de votre Torche et vous faites signe à vos
patrouilleurs de se rassembler autour de vous. Du détachement
qui vous accompagnait au début de votre mission, il ne reste plus
que quelques hommes et il vous faut être particulièrement
prudent dans les décisions que vous prendrez désormais. A peine
cependant avez-vous commencé à leur parler que vous êtes
brusquement interrompu.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome4/page_164.py", label="164", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
