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

check_inventory(current_page_number=274, book=4)

fr_text = """
Barraka dégaine son cimeterre à la lame étincelante et
tranchante comme un rasoir, puis il s'avance sur vous avec une
souplesse terrifiante qui en dit long sur sa puissance de guerrier
et son parfait sang-froid. Vous allez devoir engager contre lui un
rude combat qu'il faudra poursuivre jusqu'à la mort de l'un de
vous deux.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome4/page_122.py", label="122", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
