import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import stream_text, called_cookies, hazard_roll

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=152, book=2)

fr_text = """
L'aube vient de se lever sur le 33e jour de votre quête lorsque vous
entrez à cheval dans Port Bax en compagnie de Lord Axim. Les
préparatifs de guerre sont achevés ; les vaisseaux de la flotte de
Durenor mouillent dans le port, attendant l'ordre de mettre les voiles en
direction du Sommerlund. A bord des navires, une puissante armée de
soldats courageux et bien entraînés attend avec impatience d'affronter
au combat les Maîtres des Ténèbres. Chacun de ces hommes a juré de
libérer ses alliés assiégés par l'ennemi ou de mourir sur le champ de
bataille. Vous-même prenez place à bord du vaisseau amiral Durenor,
un grand navire à la proue arrondie et à la haute mâture dont la seule
présence donne une impression de force imposante. L'amiral Calfen qui
commande la flotte vous accueille sur le pont lorsque vous vous y
présentez accompagné de Lord Axim. Il ne reste plus à présent qu'à
donner l'ordre du départ. En moins d'une heure, les navires ont laissé le
port loin derrière eux et les dômes de Port Bax ne sont plus que de
simples points à l'horizon.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(
        stream_text(
            "Utilisez la Table de Hasard pour obtenir un chiffre. Entre 0 et 3, rendez-vous au 216. "
            "Entre 4 et 6, rendez-vous au 49. Entre 7 et 9, rendez-vous au 193."
        )
    )
    number = hazard_roll()
    if number is not None and 0 <= number <= 3:
        st.page_link("tomes/tome2/page_216.py", label="216", icon="📄")
    elif number is not None and 4 <= number <= 6:
        st.page_link("tomes/tome2/page_49.py", label="49", icon="📄")
    elif number is not None and 7 <= number <= 9:
        st.page_link("tomes/tome2/page_193.py", label="193", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
