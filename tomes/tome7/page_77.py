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

check_inventory(current_page_number=77, book=7)

fr_text = """
Une douleur fulgurante vous traverse le crâne : la main vient de s'abattre sur votre tête. Puis les doigts monstrueux s'enfoncent violemment dans votre cuir chevelu, et encore plus profondément... Votre vision se trouble et votre corps se met à trembler de tous ses membres. Les doigts griffus fouillent avidement l'intérieur de votre boîte crânienne à la recherche de la seule nourriture qui convient à cette terrifiante entité : le cerveau humain vivant ! Votre aventure et votre vie se terminent, hélas, ici.
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
