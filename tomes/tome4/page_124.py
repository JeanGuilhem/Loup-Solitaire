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

check_inventory(current_page_number=124, book=4)

fr_text = """
Un bouclier mobile muni de roues avance lentement sur le
champ de bataille semé de cadavres. Il s'approche de la barricade
et des flèches bientôt se fichent dans l'épaisseur de son panneau
de bois : ce sont les hommes du capitaine Gayal qui tirent sans
relâche pour essayer d'atteindre les attaquants dissimulés
derrière le bouclier. Soudain, une silhouette vêtue d'une toge
surgit en brandissant une baguette noire pointée vers la
barricade. L'homme est aussitôt abattu par une flèche, mais il a
eu le temps de faire jaillir de sa baguette une gigantesque boule
de feu qui traverse la plaine puis vient exploser dans un fracas
terrifiant sur la barricade. Des corps sont projetés en tous sens et
la barricade elle-même vole en éclats. A travers un nuage de
fumée et de cendres, vous distinguez bientôt une ligne de
cavaliers qui lancent une charge en galopant dans la plaine. Les
soldats sont coiffés de grands heaumes empanachés et protégés
par des plastrons d'acier d'un rouge écarlate. Dans le sillage de la
boule de feu, ils submergent les restes de la barricade en menant
une attaque sans merci. L'un des cavaliers se précipite sur vous,
la lance pointée sur votre poitrine.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez combattre cet adversaire, rendez-vous au :'))
    st.page_link("tomes/tome4/page_333.py", label="333", icon="📄")

    st.write_stream(stream_text('Si vous préférez courir vers la tour de guet, rendez-vous au :'))
    st.page_link("tomes/tome4/page_107.py", label="107", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
