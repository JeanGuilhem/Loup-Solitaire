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

check_inventory(current_page_number=346, book=4)

fr_text = """
Vous montez l'escalier en colimaçon pendant plus de cinq
minutes, avant d'atteindre un niveau supérieur où vous
découvrez un tunnel orienté au sud. Vous avez parcouru moins
de 100 mètres dans ce passage humide, lorsque vous apercevez
un levier fixé dans le mur de gauche. Soudain, vous entendez des
bruits de pas lointains : une patrouille de Gardes marche dans
votre direction. Sans hésiter un instant, vous tirez le levier et un
panneau de pierre s'ouvre aussitôt dans la paroi, révélant un
passage secret. Vous vous hâtez d'y pénétrer pour éviter les
Gardes. Dès qu'ils sont passés, vous essayez de ressortir, mais
vous vous rendez compte alors qu'il est impossible de rouvrir le
panneau de pierre de l'intérieur. Un sentiment de désespoir vous
envahit, mais vous n'en poursuivez pas moins votre chemin, le
long de ce tunnel caché.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome4/page_335.py", label="335", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
