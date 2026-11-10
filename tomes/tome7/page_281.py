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

check_inventory(current_page_number=281, book=7)

fr_text = """
Vous vous aplatissez contre le mur du tunnel et vous utilisez
votre discipline pour masquer la chaleur de votre corps. Les
serpents rampent sur vos pieds et s'enroulent autour de vos
jambes. Vous êtes pris de nausée en regardant ces répugnantes
créatures mais, pour eux, vous n'avez pas plus d'intérêt que les
dalles suintantes du sol. Les serpents continuent à avancer, vous
laissant derrière eux, tout tremblant mais indemne.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome7/page_346.py", label="346", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
