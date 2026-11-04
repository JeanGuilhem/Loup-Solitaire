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

check_inventory(current_page_number=181, book=5)

fr_text = """
Vous fouillez tous les tiroirs, forçant les serrures lorsque cela est
nécessaire mais, très déçu, vous ne retrouvez pas votre
équipement. Tout espoir de signer un traité de paix avec le
nouveau Zakhan a disparu. Vous n'avez plus qu'à continuer à
rechercher votre équipement puis fuir le Grand Palais le plus
rapidement possible afin de pouvoir retourner au Sommerlund.
Vous écartez une cloison mobile faite de lattes de bois et vous
pénétrez dans une petite pièce. D'étroites marches de pierre
mènent à une porte ouverte, dans le mur nord. Devant la porte se
trouve un coffre en bois.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous désirez gravir les marches et franchir la porte, rendez-vous au :'))
    st.page_link("tomes/tome5/page_14.py", label="14", icon="📄")

    st.write_stream(stream_text('Si vous préférez ouvrir le coffre, rendez-vous au :'))
    st.page_link("tomes/tome5/page_97.py", label="97", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
