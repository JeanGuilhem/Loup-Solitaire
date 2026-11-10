import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    lose_backpack,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=122, book=7)

fr_text = """
Vous êtes forcé de vous glisser parmi toute une horde de
créatures qui se pressent frénétiquement sur les marches menant
à la jetée. Il en sort de tous les coins : partout où vous posez les
yeux, vous voyez des mains noires et visqueuses jaillir à la
surface de la terre, cherchant à sortir de Kazan-Oud par les
multiples fissures qui déchirent le rocher. A quelques mètres de
l'escalier, vous êtes happé par un groupe d'esclaves faméliques.
Vous leur faites payer cher leur tentative, mais c'est au détriment
de votre Sac à Dos qui se trouve littéralement arraché de vos
épaules. (N'oubliez pas de rayer votre Sac à Dos de votre Feuille
d'Aventure, ainsi que tous les Objets qu'il contenait.) Lorsque
vous atteignez enfin la jetée, vous êtes couvert du sang de vos
ennemis de la tête aux pieds. Cela vous donne une allure si
terrifiante que la résistance des autres créatures fond comme
neige au soleil en vous apercevant. Sous les marches de la jetée,
vous découvrez une arche condamnée à une extrémité, mais
comportant à l'autre un porche en pierre envahi par les herbes.
A l'intérieur se trouve un canot muni de rames. Après vous être
débarrassé des quelques créatures obstinées qui tentaient encore
de s'acharner contre vous, vous mettez le bateau à l'eau, vous
sautez rapidement dedans, puis vous pagayez rageusement vers
le large, en direction de la lueur réconfortante de l'Écran de
Protection. Dans le lointain vous parviennent les cris d'agonie de Kazan-Oud.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        lose_backpack()
    st.warning("Votre Sac à Dos et tout son contenu vous ont été arrachés.")

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome7/page_350.py", label="350", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
