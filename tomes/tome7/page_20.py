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

check_inventory(current_page_number=20, book=7)

fr_text = """
Le passage mène à un gigantesque réseau de cachots où sont
enfermés les esclaves de Kazan-Oud. Ce sont pour la plupart de
misérables créatures noires et maigres, à l'échine courbée par des
années de travail sans relâche. Ces pitoyables prisonniers se
pressent contre les barreaux de leurs cellules pour dévisager le
guerrier à peau claire qui déambule librement sous leurs yeux. Ils
se mettent à siffler sur votre passage, et l'écho colporte leurs cris
tout au long du réseau souterrain. Au bout de la galerie, il y a une
espèce de cage dénuée du confort rudimentaire qu'on trouve
dans les autres cellules. En regardant à travers les barreaux, vous
apercevez un homme à la peau mate, roulé en boule sur la paille.
Ses cheveux sont blonds, et la tunique rouge et or qu'il porte est
maculée de sang et de crasse. Pendue à une corde accrochée au
mur d'à côté, vous découvrez la clé qui ouvre probablement la
cage.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous voulez prendre cette clé pour libérer le prisonnier, rendez-vous au :'))
    st.page_link("tomes/tome7/page_113.py", label="113", icon="📄")

    st.write_stream(stream_text('Si vous préférez continuer votre chemin sans vous soucier de cet homme, rendez-vous au :'))
    st.page_link("tomes/tome7/page_142.py", label="142", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
