import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_magnakai,
    show_illustrations,
    show_map,
)
from text import fr_unknown_magnakai
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=318, book=6)

fr_text = """
Le tunnel s'oriente peu à peu vers l'est, et vous remarquez qu'il
est de plus en plus éclairé. Vous apercevez une lumière verdâtre
qui filtre à travers les fines lanières d'un rideau qui ferme
presque complètement l'entrée d'une pièce voûtée.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous voulez poursuivre votre chemin, vous devez franchir le rideau. Rendez-vous alors au :'))
    st.page_link("tomes/tome6/page_349.py", label="349", icon="📄")

    st.write_stream(stream_text("Mais si, par prudence, vous préférez en écarter les lanières à l'aide de votre arme, avant de pénétrer dans la pièce voûtée, rendez-vous au :"))
    st.page_link("tomes/tome6/page_4.py", label="4", icon="📄")

    st.write_stream(stream_text('Si vous maîtrisez la Discipline Magnakaï du Contrôle Animal, rendez-vous au :'))
    if has_magnakai("Contrôle Animal"):
        st.page_link("tomes/tome6/page_32.py", label="32", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome6/page_32.py", label="32", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
