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

check_inventory(current_page_number=123, book=7)

fr_text = """
Au moment où vous appuyez sur le troisième bouton, vous
entendez un léger déclic. Le panneau s'ouvre en coulissant
doucement, révélant une volée de marches menant à une lourde
porte blindée.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez entrer dans le sarcophage, rendez-vous au :"))
    st.page_link("tomes/tome7/page_216.py", label="216", icon="📄")

    st.write_stream(stream_text("Si vous préférez ne pas vous y risquer, rendez-vous au :"))
    st.page_link("tomes/tome7/page_102.py", label="102", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
