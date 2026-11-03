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

check_inventory(current_page_number=170, book=4)

fr_text = """
Vous montez les marches de l'escalier en colimaçon pendant plus
de cinq minutes, puis vous arrivez enfin à un palier. Là, un
tunnel mène en direction du sud. Vous le suivez jusqu'à un
endroit où il tourne brusquement vers l'ouest. Un peu plus loin,
sur votre droite, un escalier descend vers un niveau inférieur.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez emprunter cet escalier, rendez-vous au :'))
    st.page_link("tomes/tome4/page_228.py", label="228", icon="📄")

    st.write_stream(stream_text('Si vous préférez continuer le long du tunnel, rendez-vous au :'))
    st.page_link("tomes/tome4/page_221.py", label="221", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
