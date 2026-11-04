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

check_inventory(current_page_number=47, book=5)

fr_text = """
Vous avez le funeste pressentiment que le nord du tunnel sert de
repaire à d'autres Kwaraz. Ce serait un suicide de continuer dans
cette direction ; aussi devez-vous choisir l'un des deux autres
chemins.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous voulez continuer par le tunnel ouest, rendez-vous au :'))
    st.page_link("tomes/tome5/page_73.py", label="73", icon="📄")
    st.write_stream(stream_text('Si vous préférez prendre le tunnel qui se dirige vers le sud, rendez-vous au :'))
    st.page_link("tomes/tome5/page_128.py", label="128", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
