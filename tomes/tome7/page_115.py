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

check_inventory(current_page_number=115, book=7)

fr_text = """
Ce dispositif de fermeture fonctionne exactement comme les
serrures mises au point par les Maîtres Serruriers de Holmgard :
il vous suffit d'appuyer une fois sur chaque bouton pour ouvrir la
porte. Mais attention, dans quel ordre allez-vous opérer ?
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez presser le premier bouton, puis le second et enfin le troisième, rendez-vous au :"))
    st.page_link("tomes/tome7/page_123.py", label="123", icon="📄")

    st.write_stream(stream_text("Si vous voulez presser le second bouton, puis le troisième et enfin le premier, rendez-vous au :"))
    st.page_link("tomes/tome7/page_231.py", label="231", icon="📄")

    st.write_stream(stream_text("Si vous voulez presser le second bouton, puis le premier et enfin le troisième, rendez-vous au :"))
    st.page_link("tomes/tome7/page_213.py", label="213", icon="📄")

    st.write_stream(stream_text("Si vous voulez presser le troisième bouton, puis le premier et enfin le second, rendez-vous au :"))
    st.page_link("tomes/tome7/page_312.py", label="312", icon="📄")

    st.write_stream(stream_text("Si vous voulez presser le troisième bouton, puis le second et enfin le premier, rendez-vous au :"))
    st.page_link("tomes/tome7/page_321.py", label="321", icon="📄")

    st.write_stream(stream_text("Si vous voulez presser le premier bouton, puis le troisième et enfin le second, rendez-vous au :"))
    st.page_link("tomes/tome7/page_132.py", label="132", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
