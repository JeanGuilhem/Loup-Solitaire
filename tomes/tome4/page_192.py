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

check_inventory(current_page_number=192, book=4)

fr_text = """
Vous êtes à moins de 2 mètres de la porte lorsqu'un brigand
surgit soudain devant vous. Instinctivement, vous faites un écart
mais vous n'êtes pas suffisamment rapide pour éviter le coup
qu'il vous porte à l'aide de sa hallebarde. L'acier glacé s'enfonce
dans votre poitrine et le sang ruisselle sur votre corps. Votre
blessure est mortelle : vous rendez l'âme quelques instants plus
tard. Votre mission s'achève ici en même temps que votre vie.
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
