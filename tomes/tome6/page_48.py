import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    pickup_button,
    pickup_gold,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=48, book=6)

fr_text = """
La salle retentit de bruits et de cris divers, mais les rixes sont
tellement fréquentes dans les tavernes de Quarle que plus personne
n'y prête attention. Une fois le chahut terminé, le fils de
l'aubergiste réapparaît et ordonne qu'on jette les corps dans la
rivière ; mais il prend soin, toutefois, de les soulager de leurs
Pièces d'Or auparavant. « Cela paiera la casse », dit-il avec un
sourire mauvais. De votre côté, vous découvrez par terre, à vos
pieds, un petit étui de cuir contenant 5 Pièces d'Or et un Plan de
Tekaro, une cité du Sud. Prenez les objets s'ils vous intéressent,
et inscrivez le Plan dans la case Sac à Dos de votre Feuille
d'Aventure, si vous souhaitez le garder.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    pickup_gold(5, key="or_etui")
    pickup_button("PLAN DE TEKARO", key="plan_tekaro", label="Prendre le Plan de Tekaro")

    st.write_stream(stream_text("Si vous voulez vous asseoir et commander un repas, rendez-vous au :"))
    st.page_link("tomes/tome6/page_172.py", label="172", icon="📄")

    st.write_stream(stream_text("Si vous préférez aller au comptoir et demander une chambre pour la nuit, rendez-vous au :"))
    st.page_link("tomes/tome6/page_232.py", label="232", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
