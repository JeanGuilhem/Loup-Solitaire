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

check_inventory(current_page_number=278, book=4)

fr_text = """
La promptitude de vos réflexes vous a sauvé d'une mort certaine.
Le disque mortel vous rate en effet et vient se loger dans une
roue. Vous éloignant du chariot, vous courez à toutes jambes le
long d'un étroit sentier qui mène à un bosquet d'arbres au
feuillage touffu. Vous plongez parmi les branchages pour vous
mettre à couvert, tandis que retentissent derrière vous les cris
des brigands.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez poursuivre votre chemin tout droit en direction du sud, parmi les arbres de la forêt, rendez-vous au :'))
    st.page_link("tomes/tome4/page_123.py", label="123", icon="📄")
    st.write_stream(stream_text("Si vous préférez aller vers l'ouest, rendez-vous au :"))
    st.page_link("tomes/tome4/page_169.py", label="169", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
