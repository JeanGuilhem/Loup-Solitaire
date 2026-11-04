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

check_inventory(current_page_number=138, book=5)

fr_text = """
Les Gardes ouvrent la porte et vous entrez aussitôt en action.
Votre poing atteint le premier homme sous la mâchoire. La
violence du coup le soulève du sol, et son épée tombe à vos pieds
avec un cliquetis métallique.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous désirez ramasser l'épée, rendez-vous au :"))
    st.page_link("tomes/tome5/page_4.py", label="4", icon="📄")

    st.write_stream(stream_text("Si vous préférez vous battre avec vos seuls poings, rendez-vous au :"))
    st.page_link("tomes/tome5/page_91.py", label="91", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
