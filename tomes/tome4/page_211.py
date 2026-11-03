import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=211, book=4)

fr_text = """
Votre stratagème a porté ses fruits. Négligeant en effet votre petit
groupe de cavaliers, les brigands poursuivent les autres
patrouilleurs en direction de l'ouest. Lorsqu'ils auront atteint les
contreforts boisés des monts Durncrag, vos hommes n'auront
aucune difficulté à fuir l'ennemi en se dissimulant dans la
végétation touffue. Dès que les brigands sont hors de vue, vous
faites halte et vous accordez à vos hommes quelques moments de
repos. Bien qu'ils ne soient plus qu'en petit nombre, vos hommes
sont impatients de poursuivre leur mission.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Utilisez la Table de Hasard pour obtenir un chiffre.'))
    roll = hazard_roll()
    if roll is not None:
        if roll <= 4:
            st.write_stream(stream_text('Si vous tirez un chiffre de 0 à 4, rendez-vous au :'))
            st.page_link("tomes/tome4/page_51.py", label="51", icon="📄")
        else:
            st.write_stream(stream_text('De 5 à 9, rendez-vous au :'))
            st.page_link("tomes/tome4/page_120.py", label="120", icon="📄")


    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
