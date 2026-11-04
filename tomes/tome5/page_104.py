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

check_inventory(current_page_number=104, book=5)

fr_text = """
« Prenez-le ! hurle Maouk, mais prenez-le vivant ! » Vous courez
vers la galère le plus rapidement possible. Les membres de
l'équipage, qui n'étaient pas présents lors du meurtre de l'envoyé,
ignorent que vous êtes dans une situation désespérée et ne
savent pas que vous courez de graves dangers. Avant même que
vous ne puissiez les appeler à l'aide, un cavalier se met en travers
de votre chemin, vous interdisant l'accès du bateau.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez attaquer le cavalier, rendez-vous au :"))
    st.page_link("tomes/tome5/page_20.py", label="20", icon="📄")

    st.write_stream(stream_text("Si vous préférez prendre la fuite en plongeant dans la mer, rendez-vous au :"))
    st.page_link("tomes/tome5/page_142.py", label="142", icon="📄")

    st.write_stream(stream_text("Enfin, si vous préférez vous rendre, rendez-vous au :"))
    st.page_link("tomes/tome5/page_176.py", label="176", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
