import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    pickup_button,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=148, book=7)

fr_text = """
Les œufs sont tièdes, et vous entendez quelque chose remuer
subrepticement sous la coquille. Avec d'infinies précautions,
vous les faites rouler sur le côté, puis vous inspectez le contenu
du nid. Parmi les débris divers, vous trouvez quelques objets
dignes d'intérêt :

- 1 Masse d'Armes (Arme)
- 1 Gilet de Cuir doublé (Objet Spécial). Ce vêtement fait gagner 2 points d'ENDURANCE lorsqu'on le porte.
- 1 Épée (Arme)
- 1 Casque (Objet Spécial). Vous gagnerez 2 points d'ENDURANCE en le coiffant.
- 1 Couverture (Objet de Sac à Dos)
- 1 Bouteille de vin (Objet de Sac à Dos)
- 1 Poignard (Arme)
- Potion de Laumspur (Objet de Sac à Dos). Elle vous fera gagner 4 points d'ENDURANCE si vous en prenez ; le flacon en contient une dose.

(Si vous souhaitez garder certains de ces Objets, n'oubliez pas de
faire les modifications nécessaires sur votre Feuille d'Aventure.)

Soudain, votre pouls s'accélère ; vous venez d'entendre du bruit
dans la chambre qui se trouve derrière vous : un verrou que l'on
tire et le grincement strident d'une porte tournant sur des gonds
rouillés.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    for index, item in enumerate(["MASSE D'ARMES", "GILET DE CUIR MATELASSÉ", "ÉPÉE", "CASQUE", "COUVERTURE",
                                  "BOUTEILLE DE VIN", "POIGNARD", "POTION DE LAUMSPUR"]):
        pickup_button(item, key=f"nid_{index}")

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre."))
    roll = hazard_roll(key="bruit")
    if roll is not None:
        if roll <= 4:
            st.write_stream(stream_text("Si ce chiffre est compris entre 0 et 4, rendez-vous au :"))
            st.page_link("tomes/tome7/page_63.py", label="63", icon="📄")
        else:
            st.write_stream(stream_text("S'il est compris entre 5 et 9, rendez-vous au :"))
            st.page_link("tomes/tome7/page_346.py", label="346", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
