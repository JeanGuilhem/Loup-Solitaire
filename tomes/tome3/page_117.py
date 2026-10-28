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

check_inventory(current_page_number=117, book=3)

fr_text = """
Le vent se calme au cours de la nuit et le jour se lève en une aube
paisible. Loin au nord, se dessinant à l'horizon, vous apercevez
Ikaya, la forteresse de glace. L'immense citadelle aux tours de
cristal offre un spectacle fascinant, rendu plus magnifique encore
par un étrange phénomène : la forteresse semble en effet avoir
été retournée et suspendue dans les airs, au-dessus d'un gros
nuage. « C'est un mirage, comme il y en a parfois dans les terres
de Kalte, vous explique Dyce ; ici, l'air est tout à fait pur, sans la
moindre poussière et la terre se reflète dans les nuages. C'est
bien Ikaya que vous voyez là-bas, mais la forteresse elle-même se
trouve au-delà de l'horizon. Elle doit être à une soixantaine de
kilomètres, environ. » Dyce saisit une pelle et entreprend de
dégager les chiens Kanu enterrés sous la neige. Vous réveillez les
autres, et tout le monde prend son petit déjeuner avant de
repartir. Vers midi, vous atteignez le bord d'une gorge profonde.
Elle est large d'une douzaine de mètres et, apparemment, il
n'existe aucun moyen de la traverser. Vous êtes donc contraint de
suivre le bord du précipice en direction de l'est. Après avoir
parcouru ainsi plus de quatre kilomètres, vous découvrez un
étroit pont de glace. Il semble malheureusement fort mince, et il
est peu probable qu'il puisse supporter le poids d'un traîneau
chargé. A présent, vous distinguez à l'horizon la forteresse
d'Ikaya mais, cette fois, ce n'est pas un mirage.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez prendre le risque de traverser le pont avec votre traîneau, rendez-vous au :"))
    st.page_link("tomes/tome3/page_73.py", label="73", icon="📄")
    st.write_stream(stream_text("Si vous préférez décharger le traîneau et transporter votre équipement de l'autre côté à raison d'un objet à la fois, rendez-vous au :"))
    st.page_link("tomes/tome3/page_162.py", label="162", icon="📄")
    st.write_stream(stream_text("Si enfin vous jugez plus sage d'abandonner votre traîneau et de continuer à pied, rendez-vous au :"))
    st.page_link("tomes/tome3/page_223.py", label="223", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
