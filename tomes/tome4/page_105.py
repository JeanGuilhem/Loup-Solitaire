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

check_inventory(current_page_number=105, book=4)

fr_text = """
Un groupe de Gardes en armes apparaît soudain en haut de
l'escalier et leur chef vous ordonne de vous arrêter. En vous
voyant hésiter, les Gardes saisissent les arbalètes qu'ils portent
en bandoulière.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez attaquer ces Gardes, rendez-vous au :'))
    st.page_link("tomes/tome4/page_285.py", label="285", icon="📄")

    st.write_stream(stream_text('Si vous préférez lever les mains et vous rendre, rendez-vous au :'))
    st.page_link("tomes/tome4/page_267.py", label="267", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
