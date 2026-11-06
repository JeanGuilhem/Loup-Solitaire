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

check_inventory(current_page_number=32, book=6)

fr_text = """
Vous sentez d'instinct que ces filaments sont en réalité des
organismes vivants formant un redoutable piège, afin de capturer
des proies destinées à quelque prédateur inconnu. Continuer dans
cette direction pourrait bien vous être fatal !
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez, malgré tout, ignorer la menace et écarter précautionneusement les filaments du bout de votre arme afin de poursuivre votre chemin, rendez-vous au :"))
    st.page_link("tomes/tome6/page_4.py", label="4", icon="📄")

    st.write_stream(stream_text("Si vous jugez plus prudent de rebrousser chemin jusqu'au croisement et de prendre l'autre tunnel, rendez-vous au :"))
    st.page_link("tomes/tome6/page_64.py", label="64", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
