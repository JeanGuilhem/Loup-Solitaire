import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    kai_rank,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=48, book=5)

fr_text = """
Vous vous concentrez sur la serrure et vous mobilisez toute votre
maîtrise Kaï pour l'ouvrir. La sueur commence à perler à votre
front.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Utilisez la Table de Hasard pour obtenir un chiffre. Si vous avez le titre de Gardien Kaï, ou un titre supérieur, ajoutez 3 points au chiffre que vous avez tiré.'))
    roll = hazard_roll()
    if roll is not None:
        bonus = 3 if kai_rank() >= 7 else 0
        total = roll + bonus
        if bonus:
            st.write(f"*Bonus : +{bonus}, soit un total de {total}.*")
        if total <= 4:
            st.write_stream(stream_text('Si le total obtenu est compris entre 0 et 4, rendez-vous au :'))
            st.page_link("tomes/tome5/page_34.py", label="34", icon="📄")
        else:
            st.write_stream(stream_text('Si le total obtenu est supérieur ou égal à 5, rendez-vous au :'))
            st.page_link("tomes/tome5/page_80.py", label="80", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
