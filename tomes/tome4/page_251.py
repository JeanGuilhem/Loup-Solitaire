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

check_inventory(current_page_number=251, book=4)

fr_text = """
Vous êtes aidés par un ciel sans nuage qui permet à la lune
d'éclairer la grand-route. Vous ordonnez à trois de vos hommes
de partir devant en éclaireurs: vous connaissez en effet la sinistre
réputation de cette route forestière sur laquelle les voyageurs
sont fréquemment surpris par des embuscades de brigands. La
forêt dense qui borde la voie pourrait dissimuler une armée
entière de voleurs. Vos éclaireurs partent donc au galop avec
pour consigne de signaler tout élément suspect qu'ils pourraient
découvrir au cours de leur reconnaissance. Une heure plus tard,
vous arrivez à un croisement où un sentier orienté à l'est s'écarte
de la grand-route. Un chariot calciné a été abandonné sur le bas-
côté. Vous sentez qu'il se passe quelque chose d'anormal. Vos
éclaireurs, en effet, auraient dû vous signaler la présence de ce
chariot bien avant que vous ne le trouviez vous-même. De toute
évidence, vos patrouilleurs sont inquiets : ils se demandent ce
qui a bien pu arriver à leurs camarades. Vous ne voulez pas
prendre le risque de continuer de peur de tomber dans une
embuscade. Vous décidez donc de vous arrêter à ce croisement
en attendant que vos éclaireurs reviennent. Six heures plus tard,
alors que le soleil s'élève lentement au-dessus de la cime des
arbres, vos hommes partis en reconnaissance n'ont toujours pas
donné signe de vie.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez poursuivre votre chemin sur la grand-route, rendez-vous au :'))
    st.page_link("tomes/tome4/page_175.py", label="175", icon="📄")
    st.write_stream(stream_text('Si vous préférez examiner les débris du chariot, rendez-vous au :'))
    st.page_link("tomes/tome4/page_38.py", label="38", icon="📄")
    st.write_stream(stream_text("Enfin, si vous estimez plus judicieux d'explorer le sentier orienté à l'est, rendez-vous au :"))
    st.page_link("tomes/tome4/page_293.py", label="293", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
