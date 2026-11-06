import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    is_new_page,
    show_illustrations,
    show_map,
    spend_gold,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=141, book=6)

fr_text = """
Cyrilus se propose de rester à surveiller les chevaux pendant
que vous prendrez part au tournoi. Il avoue que les concours de
tir ne l'intéressent guère, mais vous soupçonnez qu'il s'agit là
d'un prétexte pour aller faire une petite sieste. Vous lui
confiez les rênes de votre monture, puis vous partez rejoindre
la file des candidats. Cette compétition vous rappelle
l'ambiance des tournois de votre Sommerlund natal, où les
jongleurs, les danseurs et les multiples attractions font de ce
genre d'événement une véritable fête. Après quelques minutes
d'attente, vous arrivez enfin devant un petit guichet où une
jeune femme enjouée encaisse les droits d'inscription. Vous lui
donnez les 2 Pièces d'Or exigées pour avoir droit de participer
au tournoi, puis vous entrez sous une grande tente où les
concurrents sont déjà en train de régler la corde de leur arc.
(N'oubliez pas de rayer 2 Pièces d'Or sur votre Feuille
d'Aventure.)
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        spend_gold(2)
    st.metric(label="Pièces d'Or", value=st.session_state.purse, delta=-2)

    st.write_stream(stream_text("Si vous possédez un arc, rendez-vous au :"))
    if has_item("ARC"):
        st.page_link("tomes/tome6/page_340.py", label="340", icon="📄")
    else:
        st.page_link("tomes/tome6/page_340.py", label="340", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous n'en avez pas, rendez-vous au :"))
    if not has_item("ARC"):
        st.page_link("tomes/tome6/page_18.py", label="18", icon="📄")
    else:
        st.page_link("tomes/tome6/page_18.py", label="18", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
