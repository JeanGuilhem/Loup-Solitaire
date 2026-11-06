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

check_inventory(current_page_number=140, book=6)

fr_text = """
Vous vous hâtez le long du tunnel, comptant chaque pas pour vous
repérer, jusqu'à ce que vous arriviez à un petit passage voûté,
à quelque cent cinquante mètres du croisement précédent. Vous y
découvrez une échelle en fer, aux barreaux rongés par la
rouille. Elle s'élève jusqu'à un porche en pierre. En dessous,
le souterrain se poursuit en s'enfonçant dans les ténèbres des
égouts.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous désirez grimper à l'échelle pour aller inspecter le porche en pierre, rendez-vous au :"))
    st.page_link("tomes/tome6/page_259.py", label="259", icon="📄")

    st.write_stream(stream_text("Si vous préférez continuer à progresser dans les égouts, rendez-vous au :"))
    st.page_link("tomes/tome6/page_339.py", label="339", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
