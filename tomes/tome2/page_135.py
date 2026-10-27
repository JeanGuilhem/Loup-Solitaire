import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=135, book=2)

fr_text = """
«Voici votre abri», dit le chevalier d'un ton bourru en montrant du doigt
les bois qui s'étendent derrière vous. Avant que vous ayez pu répondre
quoi que ce soit, il fait un pas en arrière et ferme à clé la lourde porte de
la tour. La forêt qu'il vous a montrée est très dense; des herbes et des
buissons d'épines s'enchevêtrent dans les sous-bois et il faut renoncer à
y pénétrer à cheval. Il ne vous reste donc plus qu'à abandonner votre
monture et à poursuivre votre route à pied.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_244.py", label="244", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
