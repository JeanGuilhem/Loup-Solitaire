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

check_inventory(current_page_number=261, book=4)

fr_text = """
Vous trouvez les objets suivants sur le premier cadavre que vous
fouillez : 8 Pièces d'Or et des provisions équivalant à un Repas.
Vous vous apprêtez à examiner les autres corps lorsque vous
entendez des bruits de pas précipités qui s'approchent de l'autre
côté de la salle. Vous tirez à nouveau sur la corde et, à votre
grand soulagement, la herse se relève libérant l'entrée du tunnel.
Vous vous précipitez sous la lourde grille de fer et vous vous
enfuyez en courant le long du souterrain.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    pickup_gold(8, key="gold")
    pickup_button("REPAS", key="repas_1", label="Prendre 1 Repas")
    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome4/page_348.py", label="348", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
