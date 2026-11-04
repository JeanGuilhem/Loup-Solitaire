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

check_inventory(current_page_number=287, book=5)

fr_text = """
Les Itikars sont par nature des créatures farouches et
malicieuses, et un cavalier peut mettre des années à apprivoiser
et dresser l'un de ces gigantesques oiseaux. Mais une fois
domptés, ceux-ci se révèlent des créatures douces et fidèles.
L'Itikar sent que vous n'êtes pas son maître et tente de vous
repousser d'un violent coup de bec. Vous perdez 1 point
d'ENDURANCE. Néanmoins, grâce à la seule force de votre
volonté, vous parvenez à grimper sur la selle et à soumettre la
créature qui tourne la tête et vous fixe de l'œil noir et froid, mais
dénué à présent de toute hostilité. Soudain, vous voyez les
Drakkars courir sur la passerelle et vous vous penchez en avant
pour détacher la corde accrochée au pommeau de la selle avant
de saisir les épaisses rênes de cuir.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-1)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-1)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome5/page_343.py", label="343", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
