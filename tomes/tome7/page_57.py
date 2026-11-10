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

check_inventory(current_page_number=57, book=7)

fr_text = """
Vous pressentez que ces cordes et ces rochers ne sont pas ce
qu'ils paraissent, car il s'en dégage une forte aura de maléfice.
Vous tentez de percer le mystère mais votre concentration se
trouve brusquement brisée : votre esquif fait une brusque
embardée vers la jetée, et la collision n'est plus qu'une question
de secondes.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez vous jeter à l'eau afin de ne pas vous écraser contre la jetée en pierre en même temps que votre bateau, rendez-vous au :"))
    st.page_link("tomes/tome7/page_325.py", label="325", icon="📄")

    st.write_stream(stream_text("Si vous désirez saisir l'une des cordes qui pendent, rendez-vous au :"))
    st.page_link("tomes/tome7/page_203.py", label="203", icon="📄")

    st.write_stream(stream_text("Si vous préférez fermer les yeux et attendre le choc en priant pour en sortir vivant, rendez-vous au :"))
    st.page_link("tomes/tome7/page_239.py", label="239", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
