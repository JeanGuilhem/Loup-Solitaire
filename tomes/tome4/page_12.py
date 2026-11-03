import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    pickup_button,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=12, book=4)

fr_text = """
A 80 kilomètres au sud de Ruanon, la cité en ruines de Maaken
se dresse tout au bord des gorges du même nom. Vous sentez
soudain une sueur froide perler à votre front. Vous venez en effet
de vous rendre compte que, pour atteindre votre but, il vous
faudra parcourir 80 kilomètres de terrain entièrement contrôlé
par l'ennemi. Il vous reste cependant une lueur d'espoir. Vos
chances de succès devraient être à présent plus grandes qu'avant
la bataille compte tenu de la déroute des armées adverses. Avant
que vous ne vous mettiez en chemin, le capitaine Gayal vous offre
les objets suivants, parmi lesquels vous pourrez faire votre choix :
- des vivres équivalant à 3 Repas,
- 1 Corde,
- 1 Potion de Laumspur qui vous permettra de reprendre 4 points
d'ENDURANCE lorsque vous la boirez après un combat,
- 1 Epée,
- 1 Lance.
Faites votre choix et modifiez en conséquence votre Feuille
d'Aventure.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    pickup_button("REPAS", key="repas_1", label="Prendre 1 Repas")
    pickup_button("REPAS", key="repas_2", label="Prendre 1 Repas")
    pickup_button("REPAS", key="repas_3", label="Prendre 1 Repas")
    pickup_button("CORDE", key="corde", label="Prendre la Corde")
    pickup_button("POTION DE LAUMSPUR", key="laumspur", label="Prendre la Potion de Laumspur")
    pickup_button("ÉPÉE", key="epee", label="Prendre l'Épée")
    pickup_button("LANCE", key="lance", label="Prendre la Lance")

    st.write_stream(stream_text("Rendez-vous ensuite au :"))
    st.page_link("tomes/tome4/page_140.py", label="140", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
