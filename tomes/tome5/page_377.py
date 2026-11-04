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

check_inventory(current_page_number=377, book=5)

fr_text = """
Vous saisissez le bras blessé de Banedon et vous concentrez votre
pouvoir de guérison sur l'os fracturé et les muscles déchirés. La
chaleur bienfaisante que dégage votre influx atténue peu à peu sa
douleur et vous réussissez à réduire la fracture avant de
remplacer le vieux pansement ensanglanté. La blessure reste
toujours ouverte, mais le bras de Banedon est sauvé. « Nous
allons nous occuper de lui maintenant, Loup Solitaire », dit une
voix étrange. Vous êtes surpris par cette intervention et vous
vous retournez pour voir qui vient de faire cette déclaration.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome5/page_339.py", label="339", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
