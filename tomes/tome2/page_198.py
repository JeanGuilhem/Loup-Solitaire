import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=198, book=2)

fr_text = """
Vous avez à peine parcouru une vingtaine de mètres lorsque votre
cheval se cabre soudain et s'emballe. Vous êtes projeté à terre et vous
perdez 1 point d'ENDURANCE. Vous vous relevez en époussetant
votre cape et vous lancez un juron à votre monture qui disparaît au loin.
Il ne vous reste plus qu'à poursuivre votre chemin à pied.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-1)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-1)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_138.py", label="138", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
