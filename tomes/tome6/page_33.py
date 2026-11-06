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

check_inventory(current_page_number=33, book=6)

fr_text = """
Un rude choc vous attend à votre retour : Cyrilus et votre cheval
ont tous les deux disparu ! Votre première réaction est de maudire
votre compagnon, pensant qu'il est parti prendre un verre sous une
tente des environs. Mais, en voyant sa canne de chêne par terre,
sur le bas-côté de la route, vous comprenez qu'il lui est arrivé
quelque chose. Sans perdre un instant, vous grimpez sur le toit
d'un chariot bâché et vous scrutez les alentours à la recherche
d'un indice quelconque. Soudain, vous apercevez Cyrilus, entouré
d'un groupe de cavaliers, se dirigeant vers l'ouest au grand
galop. Vous comptez six hommes, plus un cheval sans cavalier :
votre cheval ! En regardant autour de vous, vous découvrez alors
un cheval sellé, attaché derrière l'un des chariots.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez enfourcher cette monture et vous lancer immédiatement à la poursuite des cavaliers, rendez-vous au :"))
    st.page_link("tomes/tome6/page_271.py", label="271", icon="📄")

    st.write_stream(stream_text("Si vous préférez partir à la recherche du propriétaire du cheval pour lui proposer de le lui racheter, rendez-vous au :"))
    st.page_link("tomes/tome6/page_325.py", label="325", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
