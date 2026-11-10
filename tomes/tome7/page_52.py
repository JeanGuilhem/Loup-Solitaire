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

check_inventory(current_page_number=52, book=7)

fr_text = """
Rassemblant toutes vos forces psychiques, vous vous concentrez
sur le tronc d'arbre. Vous parvenez à freiner sa chute et à bloquer
l'une de ses extrémités dans un renfoncement de la dernière
marche. Pendant un moment, vous le regardez se balancer de
gauche à droite comme un gigantesque métronome, puis il s'abat
en travers du gouffre dans un craquement assourdissant, tout en
soulevant un immense nuage de poussière. Lorsque la visibilité
revient, vous avez sous les yeux un pont idéal ! Sans perdre une
minute, vous franchissez le vide et vous montez rapidement
l'escalier pour atteindre la brèche qui s'ouvre dans le rempart de
la forteresse.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome7/page_27.py", label="27", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
