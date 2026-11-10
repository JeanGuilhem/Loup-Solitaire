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

check_inventory(current_page_number=22, book=7)

fr_text = """
La Main gît à vos pieds mais, malgré les nombreux coups que
vous lui avez portés, elle ne porte aucune trace de blessure.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez tourner le dos à cette épouvantable chose et pénétrer dans le tunnel qui s'ouvre devant vous, rendez-vous au :"))
    st.page_link("tomes/tome7/page_77.py", label="77", icon="📄")

    st.write_stream(stream_text('Si vous préférez examiner cette main de plus près, rendez-vous au :'))
    st.page_link("tomes/tome7/page_215.py", label="215", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
