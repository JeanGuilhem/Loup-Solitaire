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

check_inventory(current_page_number=248, book=4)

fr_text = """
Vous pénétrez dans le tunnel; en jetant un coup d'œil par-dessus
votre épaule, vous voyez se dessiner, à l'entrée de la galerie, les
silhouettes d'une horde de Guerriers. Leur redoutable cri de
guerre résonne dans les ténèbres humides. Bientôt, vous arrivez
à un endroit où le tunnel s'est effondré. Un énorme amas de terre
s'élève presque jusqu'au plafond. Vous escaladez tant bien que
mal ce monticule et vous vous glissez par l'étroit passage qui
s'ouvre à son sommet. Vous vous laissez tomber ensuite dans le
tunnel, de l'autre côté. Là, vous découvrez un étai branlant.
Lorsque tous vos hommes sont passés, vous donnez un coup
d'épaule dans le pilier de bois qui se brise aussitôt. Un déluge de
pierres et de terre se déverse dans le souterrain, bloquant
complètement le passage. Lorsque le nuage de poussière se
dissipe, vous scrutez l'obscurité qui s'étend devant vous. Vous
distinguez alors des Torches éteintes fixées aux murs. Vos
hommes les décrochent et les allument ; vous pouvez à présent
éclairer votre chemin.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome4/page_254.py", label="254", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
