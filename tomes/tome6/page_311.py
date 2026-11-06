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

check_inventory(current_page_number=311, book=6)

fr_text = """
Dans sa rage aveugle, le Yamsark plonge droit sur vous et vous le
frappez aussitôt d'un coup bien ajusté en pleine poitrine. Le
monstre est tué net, mais la force de votre coup n'est pas
suffisante pour faire basculer son énorme masse sur le côté et il
vous entraîne avec lui dans le précipice. Votre aventure et votre
vie s'achèvent ici.
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
