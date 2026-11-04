import streamlit as st
from inventory import (
    check_inventory,
    confiscate_equipment,
    display_inventory,
    end_page,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=176, book=5)

fr_text = """
Vous êtes dépossédé de votre Sac à Dos, puis on prend vos
armes, votre Or, et tous vos Objets Spéciaux. Les mains liées
dans le dos, vous êtes poussé sans ménagement, la tête la
première, dans la voiture de Maouk. « Retournez au Palais ! »
ordonne celui-ci au cocher en grimpant à l'intérieur. Il claque la
portière puis reprend: « Le Zakhan attend son prisonnier ». Vous
luttez pour essayer de dénouer la corde qui vous ligote mais
Maouk ne tarde pas à s'en apercevoir. Il saisit votre bras et vous
enfonce une aiguille dans la peau. Le rire sarcastique et cruel de
Maouk vous semble de plus en plus lointain et vous plongez
bientôt dans un profond sommeil. Mettez votre Feuille
d'Aventure à jour et faites une liste de tous les objets que l'on
vous a confisqués sur une feuille séparée qui vous servira d'aide-
mémoire au cas où vous les trouveriez plus tard au cours de votre
aventure.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        confiscate_equipment()
    st.warning("On vous a confisqué votre Sac à Dos, vos armes, votre Or et vos Objets Spéciaux : ils sont gardés de côté, vous pourrez peut-être les retrouver plus tard.")
    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome5/page_69.py", label="69", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
