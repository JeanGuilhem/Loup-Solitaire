import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=72, book=3)

fr_text = """
Vous examinez soigneusement l'autel ainsi que les deux piliers
noirs qui se dressent à sa surface. Le cyclone continue de mugir
mais, tant que vous tiendrez la Sphère de Feu dans vos mains, il
ne s'approchera pas de l'autel. Vous remarquez bientôt qu'à
l'endroit où reposait la statue deux boutons de pierre sont
apparus.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome3/page_227.py", label="227", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
