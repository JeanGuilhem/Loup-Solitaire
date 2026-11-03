import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=103, book=4)

fr_text = """
Vous arrivez à fuir le Guerrier, mais il a eu le temps de vous
infliger une blessure à l'aide de son cimeterre et vous perdez
aussitôt 4 points d'ENDURANCE. Vous étouffez un cri de
douleur, puis vous parvenez tant bien que mal à refermer la
trappe et à tirer le verrou. Vous descendez ensuite l'escalier d'un
pas chancelant et vous sortez de la tour de guet.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-4)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-4)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome4/page_59.py", label="59", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
