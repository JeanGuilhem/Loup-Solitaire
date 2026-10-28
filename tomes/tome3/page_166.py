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

check_inventory(current_page_number=166, book=3)

fr_text = """
Au pied de l'escalier, vous découvrez un autre tunnel orienté au
nord. Vous vous apprêtez à l'emprunter lorsque votre main entre
soudain en contact avec un levier qui dépasse du mur, à votre
droite. En regardant de plus près, vous constatez l'existence
d'une porte secrète.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez ouvrir cette porte, rendez-vous au :'))
    st.page_link("tomes/tome3/page_111.py", label="111", icon="📄")
    st.write_stream(stream_text('Si vous préférez poursuivre votre chemin le long du nouveau tunnel, rendez-vous au :'))
    st.page_link("tomes/tome3/page_336.py", label="336", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
