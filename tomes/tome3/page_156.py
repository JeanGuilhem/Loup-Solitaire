import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    pickup_button,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=156, book=3)

fr_text = """
Vous reconnaissez l'odeur d'un concentré de Brosse à Potences,
ou « Dent de Sommeil » comme on l'appelle plus communément
au Sommerlund. Il s'agit d'un buisson épineux dont vos Maîtres
Kaï se servaient pour endormir les chevaux malades ou blessés,
le concentré préparé à l'aide de cette plante constituant une
puissante Potion somnifère. Si vous souhaitez la conserver,
inscrivez-la sur votre Feuille d'Aventure, dans la case des objets
contenus dans votre Sac à Dos.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if not has_item("POTION DE BROSSE À POTENCES"):
        pickup_button("POTION DE BROSSE À POTENCES", key="potion_verte", label="Conserver la Potion de Brosse à Potences")
    st.write_stream(stream_text('Retournez à présent au 10 pour faire un nouveau choix :'))
    st.page_link("tomes/tome3/page_10.py", label="10", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
