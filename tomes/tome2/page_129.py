import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=129, book=2)

fr_text = """
Vous passez devant plusieurs entrepôts alignés sur le quai et vous
arrivez au mur d'enceinte du port. Là, le chemin que vous suivez tourne
brusquement à droite pour aboutir dans la rue du Tombeau. Quatre
gardes en armes marchent au milieu de la rue. Vous ne voulez pas
prendre le risque d'être interpellé et arrêté par ces soldats et vous vous
réfugiez dans une ruelle en cul-de-sac, à votre droite. Mais soudain les
gardes s'immobilisent à l'entrée de la ruelle. Il suffirait que l'un d'eux
tourne la tête dans votre direction pour que vous soyez immédiatement
repéré. Cherchant une issue, vous apercevez derrière vous une fenêtre
ouverte : un coup d'oeil à l'intérieur vous permet de distinguer la salle
comble d'une taverne. Il n'y a pas à hésiter: en un instant, vous
enjambez le rebord de la fenêtre et vous entrez dans la taverne.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_4.py", label="4", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
