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

check_inventory(current_page_number=337, book=3)

fr_text = """
L'éclaireur Barbare passe à côté de vous comme un éclair, puis il
s'immobilise quelques mètres plus loin dans un impeccable
christiania. Il déchausse aussitôt ses skis et, d'un geste rapide qui
révèle une longue pratique, il tire une épée en os à l'aspect
menaçant. Il faut vous préparer à combattre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome3/page_68.py", label="68", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
