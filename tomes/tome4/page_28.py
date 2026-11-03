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

check_inventory(current_page_number=28, book=4)

fr_text = """
Le Guerrier laisse échapper un dernier cri de douleur avant de
basculer dans le puits de mine et de disparaître dans les
ténèbres. Ses hommes semblent terrifiés par vos prouesses de
combattant et se bousculent les uns les autres dans leur hâte
d'échapper à un sort semblable. Tandis que les échos de leurs pas
précipités s'évanouissent dans le tunnel, vous traversez le pont et
vous quittez les lieux en empruntant un souterrain qui s'ouvre
dans le mur situé à l'ouest.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome4/page_348.py", label="348", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
