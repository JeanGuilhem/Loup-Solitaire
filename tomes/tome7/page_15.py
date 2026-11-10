import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    overloaded,
    pickup_button,
    restore_confiscated,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=15, book=7)

fr_text = """
Vous tournez la poignée vissée au centre de la porte et vous
entendez le déclic de la serrure. La porte s'ouvre et vous pénétrez
dans une pièce entièrement tapissée de plaques d'acier qui
brillent comme un miroir. Sur des tables basses en fer sont
disposés tous les accessoires et les instruments nécessaires à la
pratique de la magie : cornues, creusets, alambics, bonbonnes et
fioles, ainsi que tout un réseau de tubes en verre dans lesquels
passent en bouillonnant divers liquides colorés. Sur les étagères,
de gros livres reliés en vélin disputent la place à d'innombrables
rouleaux de parchemins et des bocaux où des organes rosâtres à
l'aspect peu ragoûtant baignent dans des liquides conservateurs
qui dégagent une odeur écœurante. Vous parcourez rapidement
des yeux cet échafaudage de matériel afin de trouver quelque
chose d'intéressant et, à votre plus grande joie, vous découvrez
toutes les armes que l'on vous avait confisquées. (Inscrivez à
nouveau, sur votre Feuille d'Aventure, tout ce qu'on vous avait
pris avant de vous envoyer dans le labyrinthe.) En poursuivant
vos investigations dans cet étrange laboratoire, vous découvrez
également une grosse bouteille contenant une solution
concentrée de Potion de Laumspur (il y en a suffisamment pour
vous faire récupérer 8 points d'ENDURANCE), ainsi qu'une
Amulette en Platine. Si vous souhaitez conserver cette amulette,
inscrivez-la dans la case Objets Spéciaux de votre Feuille
d'Aventure, puis mettez-la à votre poignet ; ce bracelet vous
protégera contre toute exposition à de très hautes températures.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        if restore_confiscated():
            st.success("Vous récupérez tout ce qu'on vous avait pris avant de vous envoyer dans le labyrinthe.")

    pickup_button("POTION DE LAUMSPUR CONCENTRÉE", key="potion", label="Prendre la Potion de Laumspur concentrée (+8 ENDURANCE)")
    pickup_button("AMULETTE EN PLATINE", key="amulette", label="Conserver l'Amulette en Platine")

    # l'équipement retrouvé s'ajoute à celui ramassé entre-temps : il faut d'abord faire de la place
    blocked = overloaded()
    if blocked:
        st.warning("Vous portez trop d'objets : jetez-en depuis l'onglet Inventaire avant de repartir.")

    st.write_stream(stream_text("Ravi d'avoir retrouvé votre équipement, vous quittez la pièce et vous vous engagez dans le couloir de métal étincelant. Rendez-vous au :"))
    st.page_link("tomes/tome7/page_90.py", label="90", icon="📄", disabled=blocked)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
