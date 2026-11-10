import streamlit as st
from inventory import (
    can_shoot,
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

check_inventory(current_page_number=295, book=7)

fr_text = """
Les créatures sont si absorbées par leur discussion qu'elles ne
vous voient pas entrer dans la pièce.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous avez un arc et si vous souhaitez l'utiliser, rendez-vous au :"))
    st.page_link("tomes/tome7/page_276.py", label="276", icon="📄", disabled=not (can_shoot()))

    st.write_stream(stream_text("Si vous voulez les attaquer avec une autre arme, rendez-vous au :"))
    st.page_link("tomes/tome7/page_31.py", label="31", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
