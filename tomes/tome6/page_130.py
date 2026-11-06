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

check_inventory(current_page_number=130, book=6)

fr_text = """
Lorsque les hommes d'armes réalisent qui vous êtes, leur
méfiance se mue aussitôt en respect. Votre réputation est telle
qu'elle a franchi les frontières de votre pays natal ! Les trois
mercenaires vous proposent un siège avec empressement et
appellent la serveuse à grands cris pour commander, à leurs
frais, une nouvelle tournée. Ils semblent très honorés de votre
présence et fort impatients d'entendre le récit de vos exploits.
Vous répondez à leur cascade de questions avec une réserve
polie, prenant soin de ne rien dévoiler de trop précis à propos
de votre quête. Toutefois, en dépit de leurs manières frustes et
de leur apparence bourrue, vous sentez que ces hommes sont
sincères dans l'amitié qu'ils vous témoignent.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_230.py", label="230", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
