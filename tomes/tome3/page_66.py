import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies, ls_death

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=66, book=3)

fr_text = """
Le crin qui recouvre la langue des Languabarbs contient un
puissant venin grâce auquel la créature paralyse ses victimes
avant de les dévorer. Le venin agit en quelques secondes ; or,
malheureusement pour vous, le poil rêche de la langue du
monstre vous a inoculé le poison et vous perdez très vite
conscience. Jamais vous ne vous réveillerez de ce sommeil qui
met fin à votre mission en même temps qu'à votre vie.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    show_illustrations()
    ls_death()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
