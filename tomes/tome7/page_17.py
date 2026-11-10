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

check_inventory(current_page_number=17, book=7)

fr_text = """
Au bout du couloir, un mouvement de troupe vous avertit que
d'autres gardes sont en train de pénétrer dans le sarcophage,
alertés sans doute par le bruit du combat. Plutôt que de vous
laisser surprendre dans cet étroit passage où vous ne pouvez
trouver aucun abri, vous décidez d'entrer dans la pièce et
d'essayer de fuir par le passage opposé.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome7/page_69.py", label="69", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
