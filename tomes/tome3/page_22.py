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

check_inventory(current_page_number=22, book=3)

fr_text = """
Un pouvoir magique d'une grande puissance empêche votre
esprit d'agir sur la serrure. Vous vous concentrez jusqu'à ce que
la sueur perle à votre front, mais vous êtes incapable d'obtenir le
moindre résultat. Plutôt que d'essayer d'ouvrir le coffre par la
force, vous décidez à regret de l'abandonner et vous montez
plutôt l'escalier.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome3/page_323.py", label="323", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
