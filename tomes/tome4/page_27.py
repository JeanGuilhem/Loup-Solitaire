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

check_inventory(current_page_number=27, book=4)

fr_text = """
Vous sautez à bas du chariot et vous vous précipitez vers une
forêt touffue dont la lisière se trouve à moins de 20 mètres de la
voie ferrée. La chance est avec vous : les bandits en effet n'ont
pas remarqué votre fuite audacieuse et les chariots poursuivent
leur chemin en direction du portique. Vous faites une brève halte
pour reprendre votre souffle, adressant des remerciements
silencieux à l'étranger qui vous a aidé, puis vous poursuivez votre
marche parmi les arbres.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome4/page_200.py", label="200", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
