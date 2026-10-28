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

check_inventory(current_page_number=63, book=3)

fr_text = """
Vous suivez le passage qui se prolonge vers le nord puis tourne
brusquement vers l'ouest. Un peu plus loin, un escalier de pierre
mène à une arcade située à une dizaine de mètres plus haut. De
l'autre côté de l'escalier, vous remarquez une autre porte de
pierre à côté de laquelle se trouve un levier fixé au mur. Le levier
est relevé et la porte fermée.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez monter l'escalier, rendez-vous au :"))
    st.page_link("tomes/tome3/page_323.py", label="323", icon="📄")

    st.write_stream(stream_text('Si vous préférez examiner la porte, rendez-vous au :'))
    st.page_link("tomes/tome3/page_246.py", label="246", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
