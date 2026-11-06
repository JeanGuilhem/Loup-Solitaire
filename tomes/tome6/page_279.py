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

check_inventory(current_page_number=279, book=6)

fr_text = """
Vous arrivez à une taverne qui a plus l'aspect d'une grande salle
de banquet que d'une brasserie. L'Auberge des Épées Croisées est
la plus grande et la plus bruyante que vous ayez jamais vue. Les
écuries attenantes sont si vastes qu'elles pourraient accueillir
les chevaux d'une armée entière ! Vous vous frayez un chemin dans
le flot continu de soldats qui entrent et sortent par l'immense
porte, et vous entrez dans la taverne. Vous arrivez au moment
précis où va avoir lieu un événement spectaculaire. On a poussé
les tables pour permettre à un cavalier de galoper sur toute la
longueur du bâtiment. L'assistance est invitée à parier sur
l'habileté du cavalier qui doit transpercer un fruit avec la
pointe de sa lance. Cela vous rappelle quelque peu l'exercice
d'entraînement des Seigneurs Kaï mais, contrairement à ces
derniers, il n'y a pas que l'habileté ou l'honneur qui soient en
jeu ici. Alignés contre le mur du fond, dix soldats du même
régiment sont agenouillés avec un fruit sur la tête ; ces soldats
ont été accusés de lâcheté en temps de guerre et, si le cavalier
vient à manquer d'adresse, ils perdront la vie. Mais le plus
important aux yeux des mercenaires, c'est l'argent qu'ils ont
parié sur l'adresse du cavalier.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez parier quelques Pièces d'Or dans ce jeu mortel, rendez-vous au :"))
    st.page_link("tomes/tome6/page_284.py", label="284", icon="📄")

    st.write_stream(stream_text("Si vous préférez vous approcher du bar pour parler à l'une des serveuses, rendez-vous au :"))
    st.page_link("tomes/tome6/page_299.py", label="299", icon="📄")

    st.write_stream(stream_text("Enfin, si vous souhaitez vous asseoir à l'une des tables, rendez-vous au :"))
    st.page_link("tomes/tome6/page_316.py", label="316", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
