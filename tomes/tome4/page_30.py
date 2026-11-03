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

check_inventory(current_page_number=30, book=4)

fr_text = """
Cette longue marche de nuit et le manque de sommeil
commencent à produire leurs effets sur vos hommes et leurs
chevaux. Quels que soient vos efforts pour essayer d'accélérer
l'allure de votre troupe, vous ne parvenez pas à distancer la
horde des brigands. Soudain, un groupe nombreux de cavaliers
vêtus d'armures surgit de derrière une éminence de terre, à votre
gauche. Ces soldats essaient de vous couper la route pour vous
empêcher d'avancer. Lancés les uns contre les autres, vous n'allez
pas tarder à les heurter avec violence et vous vous préparez au
choc.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome4/page_176.py", label="176", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
