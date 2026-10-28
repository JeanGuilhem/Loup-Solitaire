import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    pickup_button,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=38, book=3)

fr_text = """
Au bout de dix minutes passées à fouiller la pièce, vous
découvrez un Sac à Dos en fourrure et un long rouleau de Corde.
Vous n'avez le droit de prendre le Sac à Dos que si vous n'en avez
pas vous-même. La Corde, quant à elle, compte tenu de son
volume, occupera la place de deux objets normaux dans votre Sac
à Dos, si toutefois vous décidez de l'emporter. Voyant qu'il n'y a
plus rien à trouver dans cette pièce encombrée de bric-à-brac,
vous repartez et vous poursuivez votre exploration le long du
passage orienté à l'est.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if not st.session_state.has_backpack:
        pickup_button("SAC À DOS", key="sac", label="Prendre le Sac à Dos en fourrure")
    pickup_button("CORDE", key="corde", label="Prendre la Corde")

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome3/page_237.py", label="237", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
