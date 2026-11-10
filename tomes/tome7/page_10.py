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

check_inventory(current_page_number=10, book=7)

fr_text = """
Vous tirez une Graine de Feu de votre poche et vous la lancez
dans la gueule béante du monstre. Elle disparaît en un clin d'œil
et, quelques secondes plus tard, il vous semble que la vrille
frémit en relâchant légèrement sa pression.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        remove_from_inventory("GRAINE DE FEU")
        st.warning("Une Graine de Feu est rayée de votre Feuille d'Aventure.")

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome7/page_170.py", label="170", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
