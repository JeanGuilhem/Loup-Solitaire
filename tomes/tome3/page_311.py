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
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=311, book=3)

fr_text = """
Ce liquide vous est familier, il s'agit d'une décoction d'Alether,
une Potion de Force dont vos maîtres Kaï se servaient pour
augmenter leur HABILETÉ au combat. Cette fiole contient
suffisamment de Potion d'Alether pour augmenter de 4 points
votre total d'HABILETÉ pour la durée d'un seul combat. Vous
devrez la boire juste avant le combat pendant lequel vous
souhaiterez voir votre HABILETÉ ainsi accrue. Si vous voulez
conserver cette Potion, inscrivez-la sur votre Feuille d'Aventure
dans la liste des objets contenus dans votre Sac à Dos.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if not has_item("POTION D'ALETHER"):
        pickup_button("POTION D'ALETHER", key="alether", label="Prendre la Potion d'Alether")
    st.write_stream(stream_text("Retournez à présent au 10 et faites un nouveau choix :"))
    st.page_link("tomes/tome3/page_10.py", label="10", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
