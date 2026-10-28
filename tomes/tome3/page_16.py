import streamlit as st
from inventory import (
    check_inventory,
    choose_item_to_lose,
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

check_inventory(current_page_number=16, book=3)

fr_text = """
Vous parvenez tout juste à vous faufiler par l'entrebâillement
avant que la porte de pierre ne claque derrière vous.
Malheureusement, si vous portez un Sac à Dos sur les épaules, la
porte, en se fermant, a cassé deux des objets que vous
transportiez. Il vous faut donc les rayer de votre Feuille
d'Aventure (choisissez vous-même les objets ainsi perdus). Vous
poursuivrez ensuite votre chemin le long du passage.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    done = True
    if st.session_state.has_backpack:
        done = choose_item_to_lose(
            list(st.session_state.backpack), key="cassé_1", label="Choisissez le premier objet cassé :"
        ) and choose_item_to_lose(
            list(st.session_state.backpack), key="cassé_2", label="Choisissez le second objet cassé :"
        )
    if done:
        st.write_stream(stream_text('Rendez-vous au :'))
        st.page_link("tomes/tome3/page_63.py", label="63", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
