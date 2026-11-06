import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=295, book=6)

fr_text = """
Vous faites un bond de côté et évitez de justesse la décharge
d'énergie, mais une autre jaillit aussitôt.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous possédez le Glaive de Sommer, rendez-vous au :"))
    if has_item("GLAIVE DE SOMMER"):
        st.page_link("tomes/tome6/page_321.py", label="321", icon="📄")
    else:
        st.page_link("tomes/tome6/page_321.py", label="321", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous ne possédez pas cet Objet Spécial et que vous voulez quand même attaquer le chef, rendez-vous au :"))
    if not has_item("GLAIVE DE SOMMER"):
        st.page_link("tomes/tome6/page_257.py", label="257", icon="📄")
    else:
        st.page_link("tomes/tome6/page_257.py", label="257", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous préférez tourner les talons et fuir, rendez-vous au :"))
    st.page_link("tomes/tome6/page_182.py", label="182", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
