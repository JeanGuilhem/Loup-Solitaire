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

check_inventory(current_page_number=49, book=4)

fr_text = """
Vous vous glissez parmi les épis de blé en prenant soin de les
écarter tout d'abord de vos mains tendues. Puis vous vous
accroupissez tandis que les tiges de blé se remettent en place. Il
est désormais impossible de vous voir. Retenant votre souffle,
vous entendez les brigands passer à quelques dizaines de
centimètres de vous sans remarquer votre présence. Lorsque
vous êtes sûr qu'ils se sont suffisamment éloignés, vous sortez de
votre cachette et vous vous hâtez de poursuivre votre chemin.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome4/page_204.py", label="204", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
