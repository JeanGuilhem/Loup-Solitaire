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

check_inventory(current_page_number=58, book=7)

fr_text = """
Vous parcourez à tâtons le vide béant, mais sans succès. Soudain,
les pas que vous entendiez s'arrêtent ; un sifflement perçant,
comme le claquement d'un fouet, retentit, et une vilaine
estafilade apparaît sur le dos de votre main. (Vous perdez 2
points d'ENDURANCE.) Vous sentez la présence de l'ennemi qui
vient de vous infliger cette blessure, mais vous n'arrivez pas à le
localiser.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-2)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-2)

    st.write_stream(stream_text("Si vous voulez continuer à chercher le pont qui vous permettrait enfin de franchir le vide, rendez-vous au :"))
    st.page_link("tomes/tome7/page_44.py", label="44", icon="📄")

    st.write_stream(stream_text("Si vous préférez vous relever pour affronter votre invisible agresseur, rendez-vous au :"))
    st.page_link("tomes/tome7/page_257.py", label="257", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
