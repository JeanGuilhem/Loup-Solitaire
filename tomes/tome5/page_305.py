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
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=305, book=5)

fr_text = """
Après avoir attaché une extrémité de la corde à la rambarde du
parapet, vous lancez l'autre bout dans le vide et vous vous laissez
glisser le long de la tour. Vous êtes parvenu à mi-hauteur lorsque
vous voyez soudain, au-dessus de vous, deux Drakkars en train
de couper le nœud que vous aviez fait. La corde casse avec un
claquement sec et vous tombez comme une pierre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        remove_from_inventory("CORDE")
    st.caption("La Corde est perdue.")

    st.write_stream(stream_text('Utilisez la Table de Hasard pour obtenir un chiffre.'))
    roll = hazard_roll(key='hazard')
    if roll is not None:
        if 0 <= roll <= 2:
            st.write_stream(stream_text('Si vous avez tiré un chiffre compris entre 0 et 2, rendez-vous au :'))
            st.page_link("tomes/tome5/page_293.py", label="293", icon="📄")
        elif 3 <= roll <= 9:
            st.write_stream(stream_text('Si vous avez tiré un chiffre compris entre 3 et 9, rendez-vous au :'))
            st.page_link("tomes/tome5/page_234.py", label="234", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
