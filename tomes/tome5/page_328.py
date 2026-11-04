import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=328, book=5)

fr_text = """
Le visage du commerçant s'illumine de joie en empochant votre
or (n'oubliez pas de déduire cette somme sur votre Feuille
d'Aventure). « Prenez la première ruelle à gauche, après les
écuries, dit-il, Tipasa habite la maison à la porte bleue. » Vous
traversez rapidement la place du marché grouillante de monde,
puis vous contournez les écuries et vous vous engagez dans la
ruelle indiquée. Tout au bout de l'étroit passage sombre, vous
apercevez la maison à la porte bleue.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome5/page_206.py", label="206", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
