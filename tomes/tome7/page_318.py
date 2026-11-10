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

check_inventory(current_page_number=318, book=7)

fr_text = """
L'odeur écœurante d'humidité et de décomposition devient de
plus en plus forte, et vous êtes obligé de vous couvrir le bas du
visage avec votre manteau pour vous protéger de la puanteur. Le
tunnel tourne à droite ; vous remarquez une petite porte en fer
dans le mur devant vous et un escalier étroit qui descend dans
l'obscurité.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez examiner la porte, rendez-vous au :"))
    st.page_link("tomes/tome7/page_262.py", label="262", icon="📄")
    st.write_stream(stream_text("Si vous préférez descendre les marches, rendez-vous au :"))
    st.page_link("tomes/tome7/page_11.py", label="11", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
