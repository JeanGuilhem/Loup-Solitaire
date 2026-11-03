import streamlit as st
from inventory import (
    check_inventory,
    choose_item_to_lose,
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

check_inventory(current_page_number=22, book=4)

fr_text = """
En fouillant dans votre Sac à Dos pour y prendre une Torche,
vous faites tomber dans le vide un autre des objets qu'il contient
(si vous n'aviez qu'une Torche dans votre Sac à Dos, à l'exclusion
de tout autre objet, c'est une Arme que vous aurez perdue ; vous
choisirez vous-même l'objet tombé). Vous parvenez enfin à
allumer la nouvelle Torche et vous traversez le pont sans
encombre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    candidates = list(st.session_state.backpack)
    if "TORCHE" in candidates:
        candidates.remove("TORCHE")  # la Torche que vous allumez
    if not candidates:
        candidates = list(st.session_state.weapons)
    if choose_item_to_lose(list(dict.fromkeys(candidates)), key="chute", label="Choisissez l'objet tombé dans le vide :"):
        st.write_stream(stream_text("Poursuivez votre chemin le long du tunnel en vous rendant au :"))
        st.page_link("tomes/tome4/page_157.py", label="157", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
