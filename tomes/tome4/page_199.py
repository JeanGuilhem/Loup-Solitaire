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

check_inventory(current_page_number=199, book=4)

fr_text = """
Vous pénétrez bientôt dans une salle où un profond puits de
mine est creusé dans le sol. Une passerelle de bois permet de le
franchir, mais elle est gardée par un Guerrier. Les cris de vos
poursuivants l'ont alerté et, dès qu'il vous voit, il se précipite vers
une corde qui pend du plafond, laissant ainsi l'accès au pont
entièrement libre. Les autres Gardes vous ont presque rattrapé.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez franchir le pont en courant, rendez-vous au :'))
    st.page_link("tomes/tome4/page_271.py", label="271", icon="📄")

    st.write_stream(stream_text("Si vous préférez attaquer le Garde pour l'empêcher d'atteindre la corde, rendez-vous au :"))
    st.page_link("tomes/tome4/page_56.py", label="56", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
