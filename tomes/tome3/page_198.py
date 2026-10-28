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

check_inventory(current_page_number=198, book=3)

fr_text = """
Le couloir aboutit à une grande porte de pierre. A la différence
des autres, cette porte n'est pas actionnée par un levier ; en
revanche, vous découvrez, juste à côté, une fente creusée dans le
mur. Vous êtes en train d'examiner cette fente lorsque, soudain,
une meute hurlante de Barbares des Glaces mutants se précipite
sur vous le long du couloir. Vous vous préparez à vous défendre,
mais ils sont trop nombreux et, bien que vous les affrontiez avec
courage, ils finissent par avoir raison de vous. Inutile d'attendre
d'eux la moindre pitié : quelques instants plus tard, vous mourez
sous leurs coups. Votre mission s'achève donc ici en même temps
que votre vie.
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
