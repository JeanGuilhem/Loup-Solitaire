import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=349, book=2)

fr_text = """
Vous avez parcouru environ 5 km lorsque vous apercevez au loin une
rangée de chariots. Ils ont été placés en travers de la chaussée pour
interdire le passage, et des soldats en uniforme rouge ont pris position
sur les toits de chaque véhicule. Une foule considérable est rassemblée
derrière ce barrage et vous entendez la rumeur de conversations
animées, répercutées en écho le long du tunnel. Tandis que vous vous
approchez, le silence se fait soudain et tous les regards se tournent dans
votre direction. Un détachement d'une dizaine de soldats mené par un
chevalier qui porte un écusson frappé aux armes du royaume de
Durenor s'avance alors vers vous.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez attaquer ces soldats, rendez-vous au :"))
    st.page_link("tomes/tome2/page_87.py", label="87", icon="📄")
    st.write_stream(stream_text("Si vous préférez lever les mains en continuant de vous approcher d'eux, rendez-vous au :"))
    st.page_link("tomes/tome2/page_284.py", label="284", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
