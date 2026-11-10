import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_magnakai,
    show_illustrations,
    show_map,
)
from text import fr_unknown_magnakai
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=124, book=7)

fr_text = """
En concentrant tout votre pouvoir sur l'épée, vous pourrez lui
faire quitter le bloc de marbre et l'amener jusqu'à vous par la
voie des airs.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous décidez de recourir à votre Maîtrise de Nexus, rendez-vous au :"))
    if has_magnakai("Nexus"):
        st.page_link("tomes/tome7/page_279.py", label="279", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome7/page_279.py", label="279", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous préférez laisser l'épée où elle se trouve, vous pouvez quitter la cave par le tunnel de gauche ; rendez-vous au :"))
    st.page_link("tomes/tome7/page_298.py", label="298", icon="📄")

    st.write_stream(stream_text("Ou bien par le tunnel de droite ; rendez-vous au :"))
    st.page_link("tomes/tome7/page_322.py", label="322", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
