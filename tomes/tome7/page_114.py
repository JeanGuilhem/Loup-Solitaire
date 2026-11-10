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

check_inventory(current_page_number=114, book=7)

fr_text = """
Vos efforts sont enfin récompensés : il y a maintenant
suffisamment d'espace entre le sol et la porte pour que vous
puissiez passer en dessous. Vous pénétrez dans la chambre en
rampant puis, encore haletant de fatigue, vous vous remettez
péniblement debout. Après avoir repris votre souffle, vous vous
engagez dans le tunnel nord.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome7/page_187.py", label="187", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
