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

check_inventory(current_page_number=144, book=4)

fr_text = """
Vous sautez du chariot et vous courez à toutes jambes sans vous
douter de ce qui vous attend. Une profonde excavation s'ouvre en
effet à quelques mètres et vous y tombez tête la première. Avant
de disparaître dans ce gouffre d'une trentaine de mètres de
profondeur, vous avez le temps d'apercevoir l'expression
horrifiée de votre ami anonyme. Quelques instants plus tard,
vous vous fracassez le crâne. Votre mission s'achève ici en même
temps que votre vie.
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
