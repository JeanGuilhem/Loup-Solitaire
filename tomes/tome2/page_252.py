import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=252, book=2)

fr_text = """
Vous essayez de vous rappeler certains récits que vous a faits il y a
quelque temps un Maître Kaï surnommé «Faucon Raisonnable».
Pendant des années, il avait occupé un poste de diplomate à Port Bax et
il en était arrivé à connaître et à aimer la ville tout autant qu'un natif de
l'endroit. Vous vous souvenez de ce qu'il vous avait dit : le consulat du
Sommerlund se trouve sur la place Alin, à l'intérieur du quartier
maritime. Or, un panneau indicateur, à votre gauche, signale :
QUARTIER MARITIME 800 mètres. Certain d'être dans la bonne
direction, vous marchez d'un pas confiant le long de l'avenue bordée
d'arbres.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome2/page_191.py", label="191", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
