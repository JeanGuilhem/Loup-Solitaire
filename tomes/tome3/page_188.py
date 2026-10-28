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

check_inventory(current_page_number=188, book=3)

fr_text = """
Le lendemain d'épais nuages de neige se sont amoncelés au-dessus
de la banquise de Liouk et un faible vent s'est levé. A
mesure que vous approchez du bord du glacier de Viad, le terrain
devient plus accidenté. Des blocs de glace se dressent çà et là,
formant des obstacles difficiles à franchir. Vous êtes contraint de
descendre des traîneaux et de les manœuvrer à la main parmi
toutes ces aspérités pour pouvoir atteindre les pentes plus lisses
du lointain glacier. Vous avez parcouru environ 800 mètres
lorsque vous apercevez soudain devant vous une grande
crevasse. Elle ne fait pas plus d'une soixantaine de centimètres
de large mais elle s'étend sur plus d'un kilomètre et demi en
travers de votre chemin. Par mesure de sécurité, vos guides et
vous-même décidez de vous encorder pour la franchir. Ainsi, s'il
arrivait que l'un de vous tombe dans ce gouffre, les autres
pourraient le hisser à la surface sans trop de difficulté. Vous
n'avez aucun mal à enjamber la crevasse. Hélas ! il y en a d'autres
un peu plus loin, et en si grand nombre qu'elles forment un
véritable réseau. De fines couches de neige les dissimulent
parfois à la vue et vous ne parvenez à les repérer qu'en tâtant le
sol à l'aide de votre arme. Vous avancez ainsi pendant encore
800 mètres, puis vous arrivez devant une nouvelle crevasse qui
fait, cette fois, environ 2,50 mètres de large. Vous jetez un coup
d'œil dans ses profondeurs, mais il n'y a pas la moindre lueur
dans ce vide béant. Vos traîneaux sont longs de 3 mètres et ils
pourraient vous servir de ponts pour franchir le gouffre, mais s'il
arrivait que ses bords cèdent sous leur poids, vous risqueriez
alors de perdre d'un seul coup tout votre matériel.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez décharger les traîneaux et les utiliser comme passerelles, rendez-vous au :'))
    st.page_link("tomes/tome3/page_232.py", label="232", icon="📄")
    st.write_stream(stream_text("Si vous préférez sauter par-dessus la crevasse avec les chiens Kanu et, ensuite, tirer les traîneaux pour les amener à leur tour de l'autre côté, rendez-vous au :"))
    st.page_link("tomes/tome3/page_346.py", label="346", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
