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

check_inventory(current_page_number=348, book=5)

fr_text = """
Tout à coup, vous apercevez Banedon, le bras levé au-dessus du
parapet de la plate-forme blindée. Il tient à la main une mince
baguette bleue d'où ruisselle un torrent d'eau qui forme dans le
ciel un véritable rideau de pluie s'opposant au déluge de
flammes. Lorsqu'ils entrent en contact, une formidable explosion
se produit et un énorme tourbillon de flammes et d'eau mêlées se
met à tourner et à onduler vers le Vordak. Celui-ci hurle de
terreur, mais il est trop tard : son destin est scellé ! Le tourbillon
consume le Zlan et son cavalier dans un gigantesque brasier qui
rougeoie comme le soleil.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome5/page_267.py", label="267", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
