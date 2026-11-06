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

check_inventory(current_page_number=46, book=6)

fr_text = """
Un filet de sang s'écoule lentement au coin de la bouche du vieil
homme, puis ses yeux papillotent avant de se fermer
définitivement. Vous enterrez le corps de votre infortuné
compagnon près de l'endroit où il est tombé, dans le petit
cimetière jouxtant l'église, puis vous adressez en silence une
prière aux esprits Kaï, afin qu'ils l'accompagnent dans son
dernier voyage. Le cœur empli de tristesse, vous plantez en terre
le bâton de chêne de votre ami afin de marquer l'emplacement de sa
tombe, et vous partez ensuite, sans vous retourner, sur la
grand-route de Varetta.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_168.py", label="168", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
