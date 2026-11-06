import streamlit as st
from inventory import (
    can_shoot,
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

# Le 209 fait tirer une flèche : il faut un Arc, un Carquois et une flèche (can_shoot).

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=334, book=6)

fr_text = """
Un énorme monstre s'avance d'un pas pesant dans votre
direction. Il mesure plus de trois mètres, et ses membres épais et
tors sont recouverts de poils. Ses mains à huit doigts sont
prolongées par de redoutables griffes acérées, tranchantes
comme des lames de rasoir. Deux gros yeux jaunes et globuleux
brillent sinistrement sous son front luisant, et son corps difforme
est prolongé par une longue queue de serpent qu'il agite
frénétiquement. D'horribles rugissements rauques retentissent à
travers toute la crypte.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Préparez-vous à affronter le monstre : si vous possédez un Arc, rendez-vous au :'))
    if can_shoot():
        st.page_link("tomes/tome6/page_209.py", label="209", icon="📄")
    else:
        st.page_link("tomes/tome6/page_209.py", label="209", icon="📄", disabled=True)

    st.write_stream(stream_text('Sinon, rendez-vous au :'))
    if can_shoot():
        st.page_link("tomes/tome6/page_344.py", label="344", icon="📄", disabled=True)
    else:
        st.page_link("tomes/tome6/page_344.py", label="344", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
