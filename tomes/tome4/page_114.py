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

check_inventory(current_page_number=114, book=4)

fr_text = """
Vous ordonnez à vos hommes de se préparer au combat et vous
faites signe à l'un des fils du tenancier de la taverne d'ouvrir la
porte. A peine a-t-il fait glisser la barre de fer qui la verrouille
que la porte s'ouvre à la volée. Une douzaine de brigands,
trempés par la pluie, font alors irruption dans la taverne, leurs
boucliers en avant, alignés bord contre bord. Vos hommes se
précipitent pour tenter de les repousser ; frappant en tous sens
en direction des têtes et des bras qui émergent parfois de
derrière les boucliers ; quelques instants plus tard cependant,
d'autres bandits envahissent à leur tour la taverne et vos soldats
sont contraints de battre en retraite. Soudain, un Guerrier de
haute taille vêtu d'une armure écarlate franchit le mur de
boucliers et se précipite vers vous en brandissant son épée. Il
vous est impossible de prendre la fuite et vous devrez combattre
ce Guerrier Pillard jusqu'à la mort de l'un de vous deux.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("GUERRIER PILLARD", 16, 25)])
    if outcome == "win":
        st.write_stream(stream_text('Si vous êtes vainqueur, rendez-vous au :'))
        st.page_link("tomes/tome4/page_295.py", label="295", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
