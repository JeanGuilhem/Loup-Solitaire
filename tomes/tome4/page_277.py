import streamlit as st
from combat import combat
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

check_inventory(current_page_number=277, book=4)

fr_text = """
D'un coup de pied, vous repoussez le cadavre du Chien de Guerre
et vous vous préparez à un nouveau combat. Trois autres
molosses grognant et grondant s'apprêtent à vous bondir dessus
et vous devrez les affronter en les considérant comme un seul et
même ennemi.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("CHIENS DE GUERRE", 22, 35)])
    if outcome == "win":
        st.write_stream(stream_text('Si vous remportez la victoire, rendez-vous au :'))
        st.page_link("tomes/tome4/page_155.py", label="155", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
