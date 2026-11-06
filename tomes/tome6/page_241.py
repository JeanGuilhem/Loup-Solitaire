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

check_inventory(current_page_number=241, book=6)

fr_text = """
Vous êtes presque arrivé au sommet de la colline, lorsque vous
apercevez une petite cabane un peu en retrait de la route. Assise
sur le pas de la porte, une vieille femme épluche un fruit. Elle
vous accueille avec un large sourire, découvrant une bouche
édentée, et vous souhaite la bienvenue tandis que vous descendez
de cheval.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez lui demander si elle a vu passer des cavaliers devant chez elle, rendez-vous au :"))
    st.page_link("tomes/tome6/page_110.py", label="110", icon="📄")

    st.write_stream(stream_text("Si vous souhaitez passer votre chemin et continuer vers le sommet, rendez-vous au :"))
    st.page_link("tomes/tome6/page_3.py", label="3", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
