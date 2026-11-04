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

check_inventory(current_page_number=352, book=5)

fr_text = """
Derrière le portail, un couloir voûté mène à un large escalier.
Soudain, une douzaine de Drakkars se précipitent du palier du
deuxième étage. Vif comme l'éclair, vous plongez derrière une
statue du Zakhan Moudalla, mort récemment. Les soldats sont
tellement pressés de mettre un terme à leur poursuite qu'ils ne
découvrent même pas votre cachette et dégringolent les marches
avec leurs lourdes armures en poussant des grognements
rauques. Pendant ce temps, dissimulé dans l'ombre prodiguée
par la statue, vous vous félicitez intérieurement de la grande
taille du Zakhan Moudalla ! En haut des marches, vous apercevez
une échelle donnant accès aux toits. Vous grimpez aux barreaux,
puis vous suivez le chemin de tuiles blanchies par le soleil qui
serpente entre les tourelles et les dômes avant d'arriver à un
clocher. Vous êtes exténué et vous avez grand besoin de repos.
Encore sous le choc de votre rencontre avec le Seigneur des
Ténèbres Haakon, vous entendez résonner sans cesse à vos
oreilles le son de sa terrible voix répétant : « Le Livre de
Magnakaï ! » Découragé, vous regardez par une fenêtre grillagée
du clocher et ce que vous voyez fait naître dans votre esprit un
plan audacieux qui vous redonne confiance.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome5/page_313.py", label="313", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
