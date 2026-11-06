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

check_inventory(current_page_number=264, book=6)

fr_text = """
La créature s'arrête brusquement comme paralysée par quelque force
invisible. Elle pousse un cri de douleur, puis porte ses pattes
tremblantes à la flèche que vous lui avez décochée et tombe sur
les genoux. Elle n'a plus que quelques secondes à vivre. Le
monstre vacille puis tombe sur le dos dans la boue et les débris
qui recouvrent le sol de la chapelle, le corps secoué par un
dernier spasme.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_112.py", label="112", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
