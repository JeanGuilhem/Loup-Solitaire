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

check_inventory(current_page_number=2, book=7)

fr_text = """
L'un des murs de la pièce hexagonale attire votre attention. Au
centre du panneau en question, la maçonnerie semble bien plus
récente qu'ailleurs. Ce genre de détail n'a pas échappé à un
Maître Kaï de votre rang, et vous en déduisez aussitôt qu'il devait
jadis y avoir une porte à cet emplacement. Le bruit creux qui se
produit lorsque vous cognez à cet endroit confirme votre
hypothèse; il ne devrait pas être difficile d'enfoncer ce panneau
par quelques coups d'épaule bien ajustés.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez essayer d'enfoncer le mur, rendez-vous au :"))
    st.page_link("tomes/tome7/page_228.py", label="228", icon="📄")

    st.write_stream(stream_text('Si vous ne voulez pas vous y risquer, vous pouvez vous engager dans le couloir couleur rubis, rendez-vous au :'))
    st.page_link("tomes/tome7/page_349.py", label="349", icon="📄")

    st.write_stream(stream_text('Ou bien dans le couloir de jade, rendez-vous au :'))
    st.page_link("tomes/tome7/page_163.py", label="163", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
