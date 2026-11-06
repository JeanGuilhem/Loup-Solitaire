import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    show_illustrations,
    show_map,
    spend_gold,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=172, book=6)

fr_text = """
Vous choisissez une place dans un coin de la salle : la table y est
déjà mise, et vous aurez de là une vue d'ensemble de toute la
taverne. Une serveuse apparaît bientôt, portant un grand plat de
viande rôtie, et commence à remplir copieusement votre assiette.
« Cela fera 2 Pièces d'Or, s'il vous plaît, gentilhomme », dit-elle en
tendant une main tachée par le jus de viande. Vous la payez
aussitôt (n'oubliez pas de rayer les 2 Pièces d'Or exigées sur votre
Feuille d'Aventure), puis vous entamez votre repas avec grand
appétit. Tandis que vous vous restaurez, vous voyez l'aubergiste
approcher de votre table. C'est un petit homme gras, aux yeux
porcins. « Mon garçon d'écurie m'a dit qu'il s'était bien occupé de
votre cheval... l'est en d'bonnes mains ici, les meilleures écuries
de tout Quarle ! » Tout en vantant son établissement, l'homme se
balance nerveusement d'un pied sur l'autre, comme s'il était mal
à l'aise en votre présence, puis il vous demande : « J'suppose que
vous voulez une chambre, non ? » Vous avalez une bouchée avant
de lui rétorquer que c'est effectivement le cas. « Vous avez d'la
chance, noble Seigneur, reprend-il obséquieusement,
apparemment soulagé d'avoir trouvé en vous un bon client. Il
nous reste justement une chambre pour cette nuit, la 17. »
L'aubergiste sort une grosse clé en fer de la poche de son tablier
et la pose à côté de votre assiette. « Ce sera 3 Pièces d'Or, mon
gentilhomme, payables d'avance. » Vous réglez et vous empochez
la clé.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # 2 Pièces d'Or pour le repas et 3 pour la chambre, payées d'office (ce que la bourse permet)
    if is_new_page():
        spend_gold(min(5, st.session_state.purse))
    st.write(f"*Vous payez 5 Pièces d'Or. Il vous reste {st.session_state.purse} Pièce(s) d'Or.*")

    st.write_stream(stream_text("A présent, rendez-vous au :"))
    st.page_link("tomes/tome6/page_219.py", label="219", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
