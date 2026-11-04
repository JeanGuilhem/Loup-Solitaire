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

check_inventory(current_page_number=121, book=5)

fr_text = """
Trois Sharnazims surgissent des ténèbres. Le fil tranchant de
leurs épées brille dans l'obscurité : des lames assoiffées de sang,
votre sang !
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous désirez attaquer les guerriers, rendez-vous au :"))
    st.page_link("tomes/tome5/page_60.py", label="60", icon="📄")

    st.write_stream(stream_text("Si vous préférez les fuir, vous devez faire demi-tour et traverser l'égout à la nage. Rendez-vous en ce cas au :"))
    st.page_link("tomes/tome5/page_84.py", label="84", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
