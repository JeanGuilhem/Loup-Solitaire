import streamlit as st
from combat import combat
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

check_inventory(current_page_number=233, book=4)

fr_text = """
Vous êtes réveillé par des cris inquiets: «Debout! Debout ! On
nous attaque ! » s'exclame la sentinelle. Rejetant aussitôt leurs
couvertures, vos hommes se lèvent d'un bond, scrutant à travers
le rideau de pluie les ruines parmi lesquelles apparaissent des
silhouettes de cavaliers. Soudain, une flèche siffle dans
l'obscurité. La sentinelle pousse un cri et s'effondre. Vous donnez
aussitôt vos ordres : « Formez un cercle ! Restez à couvert ! » Les
patrouilleurs rassemblent épées et boucliers et s'abritent sous le
dôme de marbre. Des bruits de pas produits par des bottes aux
semelles ferrées résonnent alors sur le sol de pierre. Vous faites
volte-face. Une douzaine de Guerriers vêtus d'armures d'un
rouge étincelant avancent parmi les colonnes en ruine. Deux
patrouilleurs se précipitent à leur rencontre, mais ils tombent
sous les coups du chef ennemi qui les transperce de son glaive.
Le Guerrier vous aperçoit alors et hâte le pas, brandissant sa
lame ensanglantée pour frapper à nouveau. Il vous est impossible
de prendre la fuite et vous devrez combattre cet adversaire
jusqu'à la mort de l'un de vous deux.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("GUERRIER PILLARD", 17, 26)])
    if outcome == "win":
        st.write_stream(stream_text('Si vous êtes vainqueur, rendez-vous au :'))
        st.page_link("tomes/tome4/page_312.py", label="312", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
