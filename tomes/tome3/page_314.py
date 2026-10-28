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

check_inventory(current_page_number=314, book=3)

fr_text = """
Vous parcourez encore une centaine de mètres le long de la paroi
rocheuse, et vous découvrez alors une grande fissure : c'est
l'entrée d'une grotte. Dans votre impatience d'échapper à la
morsure du vent, vous vous hâtez d'y entrer et, dans l'obscurité,
vous ne remarquez pas la crevasse qui s'ouvre dans le sol de la
grotte. Vous tombez aussitôt tête la première dans les ténèbres,
accompagné d'une avalanche de glace et de pierres.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome3/page_240.py", label="240", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
