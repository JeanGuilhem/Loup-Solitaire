import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    set_flag,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

# fait posé : « cheval » (le jeune étalon pris derrière la forge noire)

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=176, book=6)

fr_text = """
Vous déclinez son offre et vous mettez en quête d'un autre moyen
pour trouver Cyrilus. Les écuries du village sont fermées et
surveillées de près mais, derrière la forge noire, vous découvrez
exactement ce que vous cherchiez. Un jeune étalon s'ébat dans
un enclos, sa selle et sa couverture sont posées sur la clôture.
Après un mouvement de recul, il sent très vite que vous ne lui
voulez aucun mal et vous n'avez aucune difficulté à le seller. Vous
sortez de l'enclos puis, après avoir contourné la forge noire, vous
vous dirigez vers la grand-route.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        set_flag("cheval")

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_271.py", label="271", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
