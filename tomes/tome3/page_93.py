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

check_inventory(current_page_number=93, book=3)

fr_text = """
Vous luttez pendant presque cinq minutes qui vous semblent
interminables tant la douleur que vous éprouvez est intense. Peu
à peu, toute volonté vous quitte, vous ne pouvez plus résister à la
domination psychique de Vonotar et vous vous jetez sur la lame
du Glaive de Sommer, ainsi qu'il vous l'ordonne. Votre mission
s'achève ici en même temps que votre vie.
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
