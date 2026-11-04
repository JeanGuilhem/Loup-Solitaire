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

check_inventory(current_page_number=174, book=5)

fr_text = """
Vous vous jetez en avant et vous donnez un violent coup de poing
au plus grand des Gardes. Votre coup l'atteint à la nuque. La
sentinelle tombe à genoux en poussant un hurlement de douleur
et lâche son épée qui tombe à vos pieds avec un bruit métallique.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez ramasser l'épée, rendez-vous au :"))
    st.page_link("tomes/tome5/page_4.py", label="4", icon="📄")

    st.write_stream(stream_text("Si vous préférez laisser l'épée, et vous battre à mains nues, rendez-vous au :"))
    st.page_link("tomes/tome5/page_91.py", label="91", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
