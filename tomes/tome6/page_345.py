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

check_inventory(current_page_number=345, book=6)

fr_text = """
L'homme est enchanté de vous montrer son travail, qui est
réellement remarquable. De nombreuses pièces ont été tuées lors
d'expéditions de chasse soit par lui, soit par des clients qui
désiraient les garder pour en faire des trophées. Il les a très
habilement maquillées afin de dissimuler toute trace de blessure.
Il vous invite ensuite à le suivre dans son atelier pour vous
montrer comment sont réalisées toutes ces merveilleuses
naturalisations.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez le suivre, rendez-vous au :'))
    st.page_link("tomes/tome6/page_213.py", label="213", icon="📄")

    st.write_stream(stream_text('Si vous préférez décliner son offre et quitter la boutique, rendez-vous au :'))
    st.page_link("tomes/tome6/page_149.py", label="149", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
