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

check_inventory(current_page_number=278, book=7)

fr_text = """
La créature commence à arracher les cocons du mur à l'aide de
ses mâchoires aiguisées comme des rasoirs. Un nuage de fibres et
de poussière tourbillonne dans l'air autour de vous, et vous
n'avez plus de cachette. Il ne vous reste plus qu'à battre en
retraite le long du couloir.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome7/page_233.py", label="233", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
