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

check_inventory(current_page_number=257, book=4)

fr_text = """
La porte n'est pas fermée à clé et elle ouvre sur une petite pièce
au sol couvert de paille. Un gros coffre aux garnitures de fer est
posé auprès d'un lit défait. De l'autre côté, vous apercevez une
deuxième porte.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez examiner le coffre, rendez-vous au :'))
    st.page_link("tomes/tome4/page_302.py", label="302", icon="📄")
    st.write_stream(stream_text('Si vous préférez ne pas y prêter attention et vous approcher de la porte, rendez-vous au :'))
    st.page_link("tomes/tome4/page_131.py", label="131", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
