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

check_inventory(current_page_number=232, book=4)

fr_text = """
Vous remontez la berge de la rivière en direction du pont de
Ruanon en prenant soin de vous dissimuler aux yeux des
brigands à cheval qui, à présent, montent la garde devant le pont
lui-même. Une centaine de mètres plus loin vous découvrez un
sentier étroit qui mène à un hangar à bateaux passablement
délabré. Si vous pouviez y trouver une embarcation, il vous serait
possible de traverser la rivière sans difficulté.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez inspecter le hangar à bateaux, rendez-vous au :'))
    st.page_link("tomes/tome4/page_68.py", label="68", icon="📄")

    st.write_stream(stream_text('Si vous préférez poursuivre votre chemin en cherchant un autre moyen de traverser la rivière, rendez-vous au :'))
    st.page_link("tomes/tome4/page_130.py", label="130", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
