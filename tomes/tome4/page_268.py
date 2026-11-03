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

check_inventory(current_page_number=268, book=4)

fr_text = """
En fouillant les Gardes, vous trouvez les objets suivants :
- 4 Pièces d'Or,
- 1 Lance,
- 1 Glaive,
- 1 Clé de Fer,
- 1 Clé de Cuivre,
- des vivres équivalant à 2 Repas
- 1 Flacon contenant un liquide rouge.
Vous reconnaissez aussitôt ce liquide : c'est une Potion de
Laumspur aux puissantes vertus curatives. Si vous la buvez après
un combat, elle vous permettra de regagner 4 points
d'ENDURANCE. Vous pouvez prendre un ou plusieurs de ces
objets, à condition de les noter sur votre Feuille d'Aventure. Une
grande porte de fer est aménagée dans le mur nord. A côté de la
porte une arcade de pierre permet d'accéder à un escalier en
colimaçon.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    pickup_gold(4, key="gold")
    pickup_button("LANCE", key="lance", label="Prendre la Lance")
    pickup_button("GLAIVE", key="glaive", label="Prendre le Glaive")
    pickup_button("CLÉ DE FER", key="cle_fer", label="Prendre la Clé de Fer")
    pickup_button("CLÉ DE CUIVRE", key="cle_cuivre", label="Prendre la Clé de Cuivre")
    pickup_button("REPAS", key="repas_1", label="Prendre 1 Repas")
    pickup_button("REPAS", key="repas_2", label="Prendre 1 Repas")
    pickup_button("POTION DE LAUMSPUR", key="laumspur", label="Prendre la Potion de Laumspur")
    st.write_stream(stream_text('Si vous souhaitez examiner la porte de fer, rendez-vous au :'))
    st.page_link("tomes/tome4/page_118.py", label="118", icon="📄")
    st.write_stream(stream_text("Si vous préférez monter l'escalier en colimaçon, rendez-vous au :"))
    st.page_link("tomes/tome4/page_170.py", label="170", icon="📄")
    st.write_stream(stream_text("S'il vous semble plus opportun de descendre l'escalier en colimaçon, rendez-vous au :"))
    st.page_link("tomes/tome4/page_228.py", label="228", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
