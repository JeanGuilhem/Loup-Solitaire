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

check_inventory(current_page_number=138, book=6)

fr_text = """
A peine la porte de l'auberge s'est-elle refermée sur vous que
vous vous trouvez nez à nez avec une patrouille de la garde
urbaine. C'est une simple question de routine pour eux : tous
les soirs, les gardes se postent devant l'Auberge des Épées
Croisées, et attendent tout bonnement que les ivrognes et les
vagabonds se fassent expulser pour les embarquer aussitôt. L'un
des soldats vous empoigne rudement par l'épaule et commence à
vous fouiller pour vous dépouiller de vos biens, avant de vous
faire monter dans la charrette qui attend non loin de là. Vous
tentez instinctivement de vous libérer, mais les hommes prennent
votre geste d'humeur pour une menace et dégainent immédiatement
leurs rapières pour passer à l'attaque. Vous ne pouvez pas
éviter le combat et vous devez vous battre jusqu'à la mort.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("PATROUILLE DE NUIT DE VARETTA", 18, 35)])
    if outcome == "win":
        st.write_stream(stream_text("Si vous sortez vainqueur de l'affrontement, rendez-vous au :"))
        st.page_link("tomes/tome6/page_34.py", label="34", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
