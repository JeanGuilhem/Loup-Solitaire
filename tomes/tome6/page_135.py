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

check_inventory(current_page_number=135, book=6)

fr_text = """
Vous avancez entre deux rangées de statues en pierre
représentant des idoles tenant dans leur bouche des torches qui
illuminent la grande avenue. Des mercenaires de toutes races y
sont rassemblés. Certains discutent, d'autres fanfaronnent ou
encore se reposent devant l'encadrement des portes. Au bout de
la rue, vous arrivez à un croisement où une femme en haillons
berce un enfant en pleurs. Au moment où vous passez devant elle,
elle se précipite vers vous en tendant la main et vous demande
quelques Pièces d'Or pour nourrir son enfant affamé.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous désirez vous arrêter pour faire l'aumône à cette pauvre femme, rendez-vous au :"))
    if st.session_state.purse >= 1:
        st.page_link("tomes/tome6/page_333.py", label="333", icon="📄")
    else:
        st.page_link("tomes/tome6/page_333.py", label="333", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous préférez passer votre chemin sans vous soucier d'elle, rendez-vous au :"))
    st.page_link("tomes/tome6/page_279.py", label="279", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
