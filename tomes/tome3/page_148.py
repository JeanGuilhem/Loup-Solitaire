import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies, ls_death

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=148, book=3)

fr_text = """
Vous avez descendu la moitié des marches lorsque vous vous
heurtez à une patrouille de Barbares des Glaces. Vous essayez de
les repousser pour pouvoir continuer votre chemin, mais ils sont
puissamment armés, disposant à la fois d'épées et de lances.
Vous vous battez avec fureur et vous en tuez un bon nombre,
mais les autres parviennent à vous encercler et à vous porter le
coup de grâce. Votre mission s'achève ici en même temps que
votre vie.
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
