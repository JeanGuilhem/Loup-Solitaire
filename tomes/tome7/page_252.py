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

check_inventory(current_page_number=252, book=7)

fr_text = """
Vous tournez la pointe de votre épée dans la serrure et vous
parvenez au bout de quelques minutes à repousser la gâche, mais
la porte ne s'ouvre toujours pas. L'effet des pilules commence à
faiblir, et vous ressentez à nouveau une douleur à la poitrine.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez continuer d'essayer d'ouvrir la porte avec votre épée, rendez-vous au :"))
    st.page_link("tomes/tome7/page_4.py", label="4", icon="📄")

    st.write_stream(stream_text("Si vous choisissez d'abandonner la porte, seule la statue peut vous offrir une possibilité de fuite ; dans ce cas, rendez-vous au :"))
    st.page_link("tomes/tome7/page_168.py", label="168", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
