import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, ls_death

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=230, book=5)

fr_text = """
Une autre explosion vient frapper la base du pilier derrière lequel
vous aviez trouvé refuge et l'énorme colonne s'écroule en
quelques secondes. Votre corps déchiqueté est enseveli sous des
tonnes de sable et de pierres. Votre vie et les espoirs du
Sommerlund s'achèvent ici.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    show_illustrations()
    ls_death()


with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
