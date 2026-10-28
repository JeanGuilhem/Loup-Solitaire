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

check_inventory(current_page_number=203, book=3)

fr_text = """
Un petit judas a été aménagé au centre de la porte. Vous y jetez
un coup d'œil prudent et vous apercevez alors le vieil homme
vêtu d'une toge bleue que vous aviez déjà vu par l'ouverture
pratiquée au-dessus de sa cellule.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez ouvrir cette porte, tirez le levier fixé au mur et rendez-vous au :"))
    st.page_link("tomes/tome3/page_56.py", label="56", icon="📄")
    st.write_stream(
        stream_text(
            "Si vous préférez ne pas vous préoccuper du vieil homme, poursuivez votre chemin le long du "
            "couloir jusqu'à la bifurcation. Rendez-vous pour cela au :"
        )
    )
    st.page_link("tomes/tome3/page_276.py", label="276", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
