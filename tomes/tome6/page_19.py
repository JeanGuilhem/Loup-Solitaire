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

check_inventory(current_page_number=19, book=6)

fr_text = """
Luyen, cité des fleurs et du vin, vous accueille avec ses jolies
maisons à colombage, ses tours élancées et son enceinte fortifiée
qui se découpent nettement dans le ciel. La ville s'étend à
l'ombre du massif des Ceners, à l'endroit même où les eaux
tumultueuses de la Storn se mêlent aux torrents turbulents qui
dévalent les pentes abruptes du mont Prindar. Le Capitaine met le
bateau à quai afin de charger les provisions à bord et, tandis que
ses hommes s'affairent à une multitude de corvées et de manœuvres
diverses, vous l'accompagnez jusqu'à la grande herboristerie de
Luyen. L'entrée de ce fameux établissement est signalée par une
énorme jarre en pierre suspendue au-dessus de la porte par de
grosses chaînes grinçantes. L'intérieur du magasin recèle une
quantité invraisemblable de produits qui excitent aussitôt votre
curiosité. Des empilements de bouteilles remplies de liquides
multicolores se dressent jusqu'au plafond ; des montagnes de sacs
de grains et des tas d'herbes et de racines de toutes sortes
jonchent le sol et couvrent de grandes étagères de bois blanchi
par l'âge. Le Capitaine désire se procurer diverses médications et
des fortifiants en vue des batailles qui les attendent, lui et ses
hommes. Les yeux de l'herboriste s'agrandissent de plaisir en
parcourant la liste d'achat de votre compagnon: ce sont les
préparations les plus chères !
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez examiner quelques-unes des potions qui s'alignent sur les étagères, rendez-vous au :"))
    st.page_link("tomes/tome6/page_2.py", label="2", icon="📄")

    st.write_stream(stream_text("Si vous préférez aller jeter un coup d'œil aux autres magasins de la rue, en attendant que l'herboriste ait fini de préparer la commande du Capitaine, rendez-vous au :"))
    st.page_link("tomes/tome6/page_152.py", label="152", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
