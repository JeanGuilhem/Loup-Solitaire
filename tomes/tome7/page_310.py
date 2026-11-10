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

check_inventory(current_page_number=310, book=7)

fr_text = """
Vous faites une boucle à l'extrémité de la corde et vous scrutez le
côté opposé à la recherche d'une prise sûre. Un éperon rocheux
près des marches effondrées semble convenir, et vous lancez
votre corde après l'avoir soigneusement visé. Le second essai est
le bon, et la corde s'enroule autour de la pierre. Sans perdre de
temps, vous franchissez le vide. Un peu plus tard, vous gravissez
les quelques marches subsistantes avant d'atteindre la brèche
s'ouvrant dans la muraille de la forteresse.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome7/page_27.py", label="27", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
