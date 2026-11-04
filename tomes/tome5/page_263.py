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

check_inventory(current_page_number=263, book=5)

fr_text = """
La vieille décrépite s'enfonce en clopinant dans l'allée sombre
tandis que Banedon et vous rebroussez chemin vers le monolithe
de l'aigle en haut duquel se trouve une flèche pointée vers l'ouest
et tournée vers la place principale. Les ombres crépusculaires
s'allongent alors que vous quittez le monolithe de l'aigle à
nouveau.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous maintenant au :"))
    st.page_link("tomes/tome5/page_216.py", label="216", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
