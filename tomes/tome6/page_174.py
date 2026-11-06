import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=174, book=6)

fr_text = """
Un cri de douleur mêlée de surprise s'échappe de votre gorge au
moment où la flèche pénètre dans votre chair. (Vous perdez 5
points d'ENDURANCE.) Cependant, votre volonté de fer et votre
entraînement Kaï vous permettent de surmonter le choc et de
rester en selle.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-5)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-5)

    st.write_stream(stream_text("Si vous êtes encore en vie après cette terrible épreuve, rendez-vous au :"))
    st.page_link("tomes/tome6/page_234.py", label="234", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
