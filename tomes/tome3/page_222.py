import streamlit as st
from inventory import (
    check_inventory,
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

check_inventory(current_page_number=222, book=3)

fr_text = """
Mettant en pratique votre Discipline Kaï, vous vous dissimulez
dans l'ombre projetée par un pilier. Les Barbares des Glaces
passent à 15 centimètres de vous, mais ils ne s'aperçoivent pas de
votre présence. Lorsque vous êtes sûr qu'ils se sont suffisamment
éloignés, vous sortez de l'ombre et vous poursuivez votre chemin
le long du couloir.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome3/page_330.py", label="330", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
