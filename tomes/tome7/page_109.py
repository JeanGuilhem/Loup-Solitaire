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

check_inventory(current_page_number=109, book=7)

fr_text = """
Vous parvenez à contenir la nausée qui vous saisit lorsque vous
sentez le ver passer près de vous en vous frôlant le dos de son
corps tiède et gluant. Dès qu'il s'éloigne, vous sortez de votre
cachette et vous remontez le tunnel en courant, soucieux de
mettre le plus de distance possible entre vous et l'ignoble créature.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome7/page_46.py", label="46", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
