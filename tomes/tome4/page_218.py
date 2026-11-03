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

check_inventory(current_page_number=218, book=4)

fr_text = """
La flèche atteint le brigand sous son bras levé. L'homme pousse
un hurlement et tombe en arrière, s'empalant sur son propre
javelot. Vous vous apprêtez à tirer une nouvelle flèche,
lorsqu'une forme noire et menaçante apparaît soudain dans le
ciel. Elle descend alors vers la tour et se pose à son sommet. Vous
jetez votre arc à terre et vous dégainez votre arme en montant
l'escalier quatre à quatre, pour aller voir de quoi il retourne.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome4/page_223.py", label="223", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
