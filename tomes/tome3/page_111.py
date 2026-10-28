import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=111, book=3)

fr_text = """
La porte glisse latéralement et révèle un large couloir bien éclairé
orienté nord-sud. Le sourd grondement que vous aviez perçu
auparavant semble plus intense ici que dans l'obscurité du
passage situé derrière vous. A votre gauche, vous remarquez une
porte et, au loin, un croisement.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez vous diriger vers ce croisement, rendez-vous au :"))
    st.page_link("tomes/tome3/page_254.py", label="254", icon="📄")
    st.write_stream(stream_text("Si vous préférez refermer la porte secrète et poursuivre votre exploration du passage obscur, rendez-vous au :"))
    st.page_link("tomes/tome3/page_336.py", label="336", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
