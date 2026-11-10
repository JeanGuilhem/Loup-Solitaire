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

check_inventory(current_page_number=288, book=7)

fr_text = """
Vous apercevez maintenant les tours et la muraille de la sinistre
forteresse, rendue plus menaçante encore par les violents éclairs
de lumière verte qui déchirent le ciel et le grondement sourd du
tonnerre dans le lointain. Un grand nombre de toits, de tourelles
sont en ruine, et leurs décombres calcinés donnent l'impression
que la forteresse a été ravagée par un incendie. Vous vous
approchez de la petite crique en forme de fer à cheval, bien
abritée au milieu de rochers noirs et déchiquetés. Au milieu de
deux d'entre eux, vous remarquez un creux asséché près du
rivage. Cet endroit est une cachette idéale pour votre petit
bateau. Silencieusement, vous sautez du coracle et vous le tirez
sur la plage vers les rochers. Mais tout à coup, vous apercevez de
minuscules lumières rouges qui dansent dans l'ombre, au pied de
la forteresse. Vous vous arrêtez net et, quelques secondes plus
tard, vous entendez des petits cris aigus et étouffés. Un éclair
illumine soudain la baie, et vous apercevez des centaines de rats
aux yeux rouges, très maigres mais tous de la taille d'un petit
chien. Ils ont l'air affamé et courent sur la plage dans votre
direction, tel un furieux torrent d'eau noire. Des gouttes de sueur
commencent à perler sur votre front, et votre cœur bat à tout
rompre : vous devez trouver rapidement un moyen d'échapper à
cette horde hurlante et féroce de rongeurs voraces.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez escalader les rochers et fuir le long d'une plage déserte, rendez-vous au :"))
    st.page_link("tomes/tome7/page_336.py", label="336", icon="📄")

    st.write_stream(stream_text("Si vous voulez remettre votre bateau à l'eau et pagayer loin de la baie, rendez-vous au :"))
    st.page_link("tomes/tome7/page_117.py", label="117", icon="📄")

    st.write_stream(stream_text("Si vous préférez rester où vous êtes pour combattre le flot de rats géants qui se précipite sur vous, rendez-vous au :"))
    st.page_link("tomes/tome7/page_45.py", label="45", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
