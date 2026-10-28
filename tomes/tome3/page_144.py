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

check_inventory(current_page_number=144, book=3)

fr_text = """
Vous êtes précipité dans les ténèbres et vous vous écrasez contre
une corniche de glace après une chute de plus de 30 mètres.
Votre corps disloqué rebondit pour tomber plus bas encore, mais
votre colonne vertébrale a été fracassée sous le choc et vous êtes
donc déjà mort lorsque vous atterrissez enfin sur la neige molle
qui tapisse le fond de la crevasse. Votre mission s'achève ici en
même temps que votre vie.
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
