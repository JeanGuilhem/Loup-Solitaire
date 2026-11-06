import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    receive_gold,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=34, book=6)

fr_text = """
Le bruit de la bataille a attiré l'attention de nombreux
mercenaires et de leurs capitaines. Tous sont penchés aux fenêtres
et vous acclament bruyamment tandis que vous expédiez ad patres le
dernier membre de la garde. Tout en essuyant la lame de votre
arme, vous remarquez que l'une de vos victimes porte à la ceinture
une bourse bien rebondie. Prenez-la, puis utilisez la Table de
Hasard pour obtenir un chiffre et ajoutez 5 au nombre que vous
avez tiré. Le résultat représente le nombre de Pièces d'Or
contenues dans cette bourse. Soudain les portes de la taverne
s'ouvrent à la volée et un Capitaine mercenaire vous fait signe
d'entrer rapidement avant qu'une autre patrouille arrive et
découvre votre œuvre. L'homme semble fort impressionné par votre
prouesse et vous propose de venir prendre un verre avec lui. Vous
sentez qu'il s'agit là d'une offre honnête et amicale, aussi
acceptez-vous volontiers cette invitation.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    roll = hazard_roll(key="bourse", label="Ouvrir la bourse (Table de Hasard + 5)")
    if roll is not None:
        receive_gold(roll + 5, key="bourse")

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_211.py", label="211", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
