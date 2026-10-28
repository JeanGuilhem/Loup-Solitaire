import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=269, book=3)

fr_text = """
Vous découvrez un tunnel, de l'autre côté du gouffre, et vous le
suivez sur des kilomètres. Vous arrivez enfin dans une immense
caverne dont la voûte s'élève à 150 mètres au-dessus de votre
tête. Un vent glacial, s'infiltrant à travers les nombreuses fissures
de cette voûte, souffle dans la caverne.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez essayer de grimper jusqu'à la voûte pour tenter de vous glisser par l'une de ces fissures et sortir ainsi à l'air libre, rendez-vous au :"))
    st.page_link("tomes/tome3/page_335.py", label="335", icon="📄")

    st.write_stream(stream_text('Si vous préférez poursuivre votre chemin en essayant de trouver un autre tunnel au fond de la caverne, rendez-vous au :'))
    st.page_link("tomes/tome3/page_182.py", label="182", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
