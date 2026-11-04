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

check_inventory(current_page_number=5, book=5)

fr_text = """
Vous avez à moitié contourné la tour, lorsqu'une pierre de la
corniche se détache soudain sous vos pieds. Vous vous agrippez
désespérément à la paroi, mais la maçonnerie est vieille ; elle se
désagrège sous vos doigts et vous basculez en arrière, tombant,
pour votre plus grand malheur, dans les jardins du Palais qui
s'étendent en dessous. Votre évasion prend fin ici ; votre
aventure aussi.
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
