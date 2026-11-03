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

check_inventory(current_page_number=201, book=4)

fr_text = """
Les champignons sont mous, secs et leur goût est détestable. Ils
se transforment dans votre bouche en une poudre sèche qui
absorbe toute votre salive. Vous êtes pris de haut-le-cœur, vous
toussez et une nausée vous saisit. Gagné par la panique, vous
vous hâtez de recracher les champignons, puis vous poursuivez
votre chemin le long du tunnel.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome4/page_65.py", label="65", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
