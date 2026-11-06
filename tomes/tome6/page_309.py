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

check_inventory(current_page_number=309, book=6)

fr_text = """
« Eh bien, vous n'avez pas de chance cette nuit, étranger, les dés
m'ordonnent de tenir ma langue ! » Ils éclatent tous de rire puis
continuent leur partie. Vous haussez les épaules et vous
continuez à avancer dans la rue grouillante de monde.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome6/page_307.py", label="307", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
