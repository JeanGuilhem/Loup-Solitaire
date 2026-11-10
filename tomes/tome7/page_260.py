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

check_inventory(current_page_number=260, book=7)

fr_text = """
Une odeur rance de moisi empeste l'atmosphère, et vous
découvrez, déçu, que le tunnel n'est en fait qu'une grotte peu
profonde servant de nid à des œufs gigantesques, aussi gros que
des fûts de bière. Les œufs sont posés sur un tas de vieux
vêtements déchirés et d'affaires diverses, appartenant
probablement aux aventuriers précédents qui se sont heurtés au
serpent géant.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez examiner ces objets de plus près, rendez-vous au :"))
    st.page_link("tomes/tome7/page_148.py", label="148", icon="📄")

    st.write_stream(stream_text("Si vous voulez chercher un moyen de fuir le tunnel, rendez-vous au :"))
    st.page_link("tomes/tome7/page_346.py", label="346", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
