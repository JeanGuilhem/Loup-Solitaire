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

check_inventory(current_page_number=62, book=5)

fr_text = """
Votre intuition et votre expérience vous avertissent qu'il serait
follement imprudent d'attaquer les Gardes à proximité de la
cantine, car les bruits de bataille alerteraient immédiatement les
nombreux soldats qui s'y trouvent. Il ne vous reste plus qu'une
chose à faire : vous dissimuler sur la corniche extérieure qui
longe le mur du Palais.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome5/page_152.py", label="152", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
