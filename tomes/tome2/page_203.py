import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=203, book=2)

fr_text = """
« Vous avez faim ! Voulez-vous un peu de fromage ? » Vous avez posé
cette question au marin après avoir jeté un coup d'œil aux deux souris
qui s'affairent à l'autre bout de la salle. Utilisant alors la Discipline Kaï
de la Communication Animale, vous ordonnez aux deux rongeurs de
vous apporter leur fromage et, un instant plus tard, l'homme constate
avec stupéfaction que les souris viennent effectivement déposer le
fromage à vos pieds avant de disparaître en toute hâte.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome2/page_268.py", label="268", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
