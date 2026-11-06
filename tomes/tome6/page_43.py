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

check_inventory(current_page_number=43, book=6)

fr_text = """
Aucune réponse ne vous parvient. Vous contournez alors le comptoir
et vous jetez un œil dans l'arrière-salle, mais celle-ci est
déserte également. Tout cela semble bien étrange... Vos soupçons
se confirment lorsque vous constatez que la porte du four est
restée grande ouverte ainsi que la porte du fond de la pièce. Par
ailleurs, un fauteuil a été renversé et tout porte à croire que
l'on s'est récemment battu dans cette pièce... Alors que vous vous
apprêtez à inspecter l'endroit plus attentivement, vous percevez
un faible appel au secours. C'est Cyrilus, il est sûrement en
difficulté !
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_317.py", label="317", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
