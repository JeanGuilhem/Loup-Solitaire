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

check_inventory(current_page_number=140, book=7)

fr_text = """
Craignant qu'une mort atroce ne vous surprenne à tout moment,
vous gardez tous vos sens en alerte afin de déceler le moindre
signe de danger. Vous apercevez justement devant vous un rayon
de lumière barrant le chemin à hauteur du genou.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez sauter par-dessus ce rayon, rendez-vous au :"))
    st.page_link("tomes/tome7/page_155.py", label="155", icon="📄")

    st.write_stream(stream_text("Si vous décidez de passer à travers, rendez-vous au :"))
    st.page_link("tomes/tome7/page_94.py", label="94", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
