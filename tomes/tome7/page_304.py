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

check_inventory(current_page_number=304, book=7)

fr_text = """
Les bruits de pas cessent mais un claquement sec ressemblant à
un coup de fouet rompt le silence. Vous poussez un cri de
douleur mêlé de surprise tandis qu'une vilaine zébrure rouge
vous déchire la peau de la tempe au menton. (Vous perdez 3
points d'ENDURANCE.) Vous sentez la présence ennemie, mais
vous ne voyez pas celui qui vous a infligé cette blessure.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-3)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-3)

    st.write_stream(stream_text("Si vous souhaitez vous défendre contre cet attaquant invisible, rendez-vous au :"))
    st.page_link("tomes/tome7/page_257.py", label="257", icon="📄")
    st.write_stream(stream_text("Si vous voulez rebrousser chemin en courant le long du couloir, rendez-vous au :"))
    st.page_link("tomes/tome7/page_64.py", label="64", icon="📄")
    st.write_stream(stream_text("Si vous préférez prendre le risque de sauter dans le vide, rendez-vous au :"))
    st.page_link("tomes/tome7/page_275.py", label="275", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
