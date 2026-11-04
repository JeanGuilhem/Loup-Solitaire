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

check_inventory(current_page_number=78, book=5)

fr_text = """
Vous passez rapidement à l'attaque et, d'un violent coup sur la
nuque, vous réduisez le Garde au silence avant qu'il ait eu le
temps de donner l'alerte.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez prendre la fuite sans vous soucier des dépouilles des Gardes que vous avez éliminés, rendez-vous au :"))
    st.page_link("tomes/tome5/page_150.py", label="150", icon="📄")

    st.write_stream(stream_text("Si vous désirez les fouiller auparavant, rendez-vous au :"))
    st.page_link("tomes/tome5/page_102.py", label="102", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
