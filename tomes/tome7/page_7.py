import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=7, book=7)

fr_text = """
Vous découvrez, à votre grande consternation, que votre carquois
est vide; les flèches ont dû s'en échapper lorsque vous êtes tombé
dans le nid. (Rayez toutes vos flèches de votre Feuille
d'Aventure.)
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        st.session_state.arrows = 0
        st.warning("Toutes vos flèches sont rayées de votre Feuille d'Aventure.")

    st.write_stream(stream_text("Avec un geste de dépit, vous rejetez votre arc et vous dégainez une arme de poing, juste avant que l'immonde reptile ne passe à l'attaque. Rendez-vous au :"))
    st.page_link("tomes/tome7/page_301.py", label="301", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
