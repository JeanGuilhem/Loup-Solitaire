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

check_inventory(current_page_number=197, book=6)

fr_text = """
Vous êtes presque hors de portée des arcs lorsqu'une flèche vous
entaille le mollet, avant de s'enfoncer avec un bruit mat dans le
ponton. Vous vous mordez les lèvres pour réprimer un cri de
douleur afin de ne pas alerter les archers de la ville située sur
l'autre rive. Dès que le ponton touche la berge, vous sautez à
terre puis vous vous faufilez à travers les rochers vers l'endroit où
se déversent les égouts.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_249.py", label="249", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
