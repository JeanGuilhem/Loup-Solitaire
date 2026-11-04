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

check_inventory(current_page_number=171, book=5)

fr_text = """
Un panneau, situé derrière la statue, glisse sur le côté et révèle
l'existence d'un passage secret, étroit et obscur. Vous pouvez
quand même voir nettement deux empreintes de pas dans la
poussière qui recouvre le sol.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez suivre le passage secret, rendez-vous au :'))
    st.page_link("tomes/tome5/page_148.py", label="148", icon="📄")

    st.write_stream(stream_text('Sinon, refermez le panneau et continuez à avancer dans la galerie. Rendez-vous au :'))
    st.page_link("tomes/tome5/page_158.py", label="158", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
