import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    pickup_button,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=279, book=7)

fr_text = """
En réponse à votre pouvoir psychique, l'épée s'élève du bloc et
glisse vers votre main. C'est une arme ordinaire, de qualité
médiocre, et sa lame épaisse est indigne de votre fourreau mais,
dans ce labyrinthe étrange et hostile, cela suffit à faire renaître
vos espoirs de survie.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    pickup_button("ÉPÉE", key="epee", label="Prendre l'Épée")

    st.write_stream(stream_text("Si vous souhaitez quitter la pièce par le tunnel gauche, rendez-vous au :"))
    st.page_link("tomes/tome7/page_298.py", label="298", icon="📄")

    st.write_stream(stream_text("Si vous préférez suivre le tunnel de droite, rendez-vous au :"))
    st.page_link("tomes/tome7/page_322.py", label="322", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
