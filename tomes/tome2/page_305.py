import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    receive_gold,
    show_illustrations,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=305, book=2)

fr_text = """
Un silence pesant s'installe dans la taverne, il en faut davantage
cependant pour vous impressionner et c'est avec le plus grand calme
que vous ramassez les 5 Pièces d'Or posées sur la table. Vous vous
dirigez ensuite vers la porte, mais, au moment où vous allez sortir, un
marin d'une laideur repoussante vous bloque le passage en brandissant
une épée. Un instant plus tard, alors que vous vous demandez ce qu'il
convient de faire, un coup sourd résonne dans le silence de la salle et
l'homme tombe à genoux sur le plancher. Vous avez la surprise de
reconnaître, debout derrière lui, la servante qui tient fermement des
deux mains une grosse massue de bois. Vous la remerciez d'un sourire
complice, mais le temps n'est pas aux effusions et vous vous hâtez de
disparaître dans l'ombre de la rue, tandis qu'à l'intérieur de la taverne
des voix s'élèvent pour vous maudire. Après avoir couru pendant dix
minutes dans le noir, vous apercevez un peu plus loin une grande écurie
et un relais de diligence ; derrière vous retentissent des cris de marins
furieux qui vous poursuivent dans la rue : pour leur échapper, vous
montez quatre à quatre une échelle extérieure qui mène à un grenier.
Là, vous pourrez passer la nuit en toute sécurité, blotti parmi des bottes
de foin.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    receive_gold(5)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_32.py", label="32", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
