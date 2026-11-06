import streamlit as st
from inventory import (
    can_shoot,
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

check_inventory(current_page_number=153, book=6)

fr_text = """
Le carreau d'arbalète fend l'air comme un éclair et vous érafle les
côtes, vous arrachant un bout de chair au passage avant d'aller se
planter dans la cabane en bois. (Vous perdez 5 points
d'ENDURANCE.) Réprimant à grand-peine un cri de douleur,
vous vous dirigez tant bien que mal vers votre cheval.
Entretemps, votre adversaire a rangé son arbalète et il éperonne
furieusement sa monture pour aller rejoindre ses compagnons de
l'autre côté du pont.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-5)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-5)

    st.write_stream(stream_text("Si vous possédez un arc, rendez-vous au :"))
    st.page_link("tomes/tome6/page_178.py", label="178", icon="📄", disabled=not can_shoot())

    st.write_stream(stream_text("Si vous n'avez pas d'arc, enfourchez votre cheval, lancez-vous à la poursuite des cavaliers et rendez-vous au :"))
    st.page_link("tomes/tome6/page_39.py", label="39", icon="📄", disabled=can_shoot())

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
