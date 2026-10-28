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

check_inventory(current_page_number=240, book=3)

fr_text = """
Vous faites une chute de plus de 10 mètres et vous atterrissez sur
le dos au fond de la crevasse, au milieu d'un tas de neige
poudreuse. Vous êtes entouré de stalagmites et de pointes de
glace qui hérissent les parois, mais par miracle vous êtes
indemne. Quelque peu secoué par le choc, mais reconnaissant
d'être toujours en vie, vous vous relevez en vous accrochant à une
stalagmite. Vous vous rendez compte alors que vous voyez à peu
près clairement autour de vous : une faible lumière filtre en effet
à travers une ouverture située à votre gauche. La curiosité
l'emporte sur votre prudence naturelle et vous vous approchez de
cette lueur d'un pas chancelant. Vous découvrez là une grotte
dans laquelle vous pénétrez.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome3/page_284.py", label="284", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
