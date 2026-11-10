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

check_inventory(current_page_number=38, book=7)

fr_text = """
Vos pouvoirs psychiques vous révèlent que vous n'avez devant
vous qu'une simple illusion. L'Oudakon est, en effet, une force
spectrale placée ici par un puissant magicien et qui prend forme
dès que quelqu'un ou quelque chose approche la porte de la
Grande Galerie. Grâce à un grand effort de concentration, vous
parvenez à ordonner à l'illusion de disparaître. Aussitôt l'ombre - qui semblait si réelle il y a quelques secondes - se dissout en une
légère brume que l'air de la nuit ne tarde pas à emporter.
Simultanément, vous entendez s'élever un cri de colère dont
l'écho va en s'évanouissant à travers les ruines du donjon.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome7/page_293.py", label="293", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
