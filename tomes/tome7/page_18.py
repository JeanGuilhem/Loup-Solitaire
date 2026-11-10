import streamlit as st
from inventory import (
    change_endurance,
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

check_inventory(current_page_number=18, book=7)

fr_text = """
Les mots du crâne faisant écho dans votre esprit, vous ôtez le
bouchon de la bouteille avec les dents, puis vous versez le liquide
dans le gouffre en décrivant un grand arc de cercle de la gauche
vers la droite. Vous êtes certain qu'il existe un pont invisible qui
franchit le vide... mais il vous faut arriver à le localiser. Soudain,
les bruits de pas que vous aviez perçus s'arrêtent. Vous entendez
un craquement sonore, comme le claquement d'un fouet et,
immédiatement après, une vilaine zébrure rouge apparaît sur
votre poignet (vous perdez 2 points d'ENDURANCE). La
bouteille vous échappe des mains et il vous semble qu'elle
rebondit à mi-hauteur avant de tomber dans le vide : vous venez
de trouver le pont ! Malheureusement, il va falloir tenir compte
de l'ennemi invisible qui vient de vous attaquer.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-2)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-2)

    st.write_stream(stream_text('Si vous voulez avancer sur le pont, rendez-vous au :'))
    st.page_link("tomes/tome7/page_166.py", label="166", icon="📄")

    st.write_stream(stream_text('Si vous préférez affronter auparavant votre mystérieux agresseur, rendez-vous au :'))
    st.page_link("tomes/tome7/page_257.py", label="257", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
