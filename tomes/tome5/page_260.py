import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    remove_from_inventory,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=260, book=5)

fr_text = """
Après avoir rassemblé et revêtu les divers éléments de
l'équipement spécial pour les fouilles, vous avancez discrètement
vers la sentinelle et vous videz la Teinture dans la cruche d'eau
placée à ses pieds.
Quelques instants plus tard, l'homme se penche pour saisir la
cruche puis en avale quelques gorgées. L'effet ne se fait pas
attendre : le Garde se sent tout à coup très mal. Tandis qu'il
titube en arrière, vous vous glissez dans le Tombeau sans être
repéré.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        remove_from_inventory("POTION DE RONCES DES CIMETIÈRES")

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome5/page_395.py", label="395", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
