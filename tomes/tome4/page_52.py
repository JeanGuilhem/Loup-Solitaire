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

check_inventory(current_page_number=52, book=4)

fr_text = """
Une pluie de flèches empennées s'abat sur vous et trois de vos
hommes ont été touchés lorsque vous atteignez la mine. Une
autre flèche passe si près de votre tête qu'elle vous érafle l'œil
droit. Vous êtes aveuglé et vous perdez 1 point d'ENDURANCE.
Protégeant de la main votre œil blessé, vous approchez en
chancelant de l'entrée du tunnel.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-1)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-1)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome4/page_248.py", label="248", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
