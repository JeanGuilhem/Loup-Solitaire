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

check_inventory(current_page_number=81, book=6)

fr_text = """
Les flèches sifflent de toutes parts. L'une d'elles inflige une
profonde entaille sur la croupe de votre cheval, qui se met
aussitôt à se cabrer furieusement. Raccourcissant les rênes,
vous parvenez à reprendre le contrôle de l'animal effarouché, à
le lancer au galop et à vous mettre enfin hors de portée des
projectiles meurtriers.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_39.py", label="39", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
