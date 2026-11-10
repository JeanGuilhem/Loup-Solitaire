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

check_inventory(current_page_number=102, book=7)

fr_text = """
Le panneau se referme de lui-même en coulissant lentement,
puis les boutons reviennent à leur place initiale en produisant un
léger déclic.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez sortir du vestibule en empruntant le tunnel qui se trouve à votre gauche, rendez-vous au :"))
    st.page_link("tomes/tome7/page_201.py", label="201", icon="📄")

    st.write_stream(stream_text("Si vous préférez vous engager dans le tunnel de droite, par où les gardes en armure noire ont surgi, rendez-vous au :"))
    st.page_link("tomes/tome7/page_323.py", label="323", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
