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

check_inventory(current_page_number=263, book=7)

fr_text = """
Votre cerveau n'est plus alimenté en oxygène, et votre vue baisse
rapidement. Vous êtes pris de vertige, et la douleur qui vous
brûle la poitrine cesse enfin tandis que vous sombrez dans
l'inconscience. Vos poumons sont maintenant remplis d'eau, et
vous coulez lentement vers le fond. Votre vie ainsi que votre
aventure s'achèvent ici.
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
