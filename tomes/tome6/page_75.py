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

check_inventory(current_page_number=75, book=6)

fr_text = """
Votre flèche part à la vitesse de l'éclair et transperce l'œil
de la créature. Un hurlement de douleur et de rage vous brise
les tympans, tandis que le monstre recule en titubant, la face
transformée en un masque sanguinolent. Puis il tombe à la
renverse, le corps secoué de spasmes, sur le sol boueux jonché
de débris.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_112.py", label="112", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
