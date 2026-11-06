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

check_inventory(current_page_number=203, book=6)

fr_text = """
Vous retenez votre souffle pendant que vos ennemis passent
devant vous et, lorsque le dernier homme de la colonne arrive à
votre niveau, vous sortez brusquement de votre cachette et vous
vous jetez sur lui. Il tente bien de se protéger avec son bouclier,
mais il réagit trop lentement et ne peut parer le coup mortel que
vous lui assenez. Il tombe au sol, et vous coupez les sangles de sa
selle avant de reprendre la route avec le magicien toujours
inconscient, ligoté sur le cheval.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_188.py", label="188", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
