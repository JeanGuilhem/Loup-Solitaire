import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=72, book=7)

fr_text = """
Le poing enflammé de la créature roussit votre tunique, mais
votre maîtrise Kaï vous permet heureusement de survivre à la
brûlure. (Vous perdez cependant 2 points d'ENDURANCE.)
Heureusement pour vous, votre adversaire mène son attaque de
façon aveugle et désordonnée, et vous parvenez aisément à
esquiver les coups suivants. Plongeant rapidement sous le bras
de la créature, vous vous élancez vers les jets de flammes, dans
l'espoir de pouvoir prendre la fuite, mais la vue de l'enfer qui
vous attend vous fait hésiter.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-2)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-2)

    st.write_stream(stream_text("Si vous voulez entrer dans le brasier, rendez-vous au :"))
    st.page_link("tomes/tome7/page_204.py", label="204", icon="📄")

    st.write_stream(stream_text("Si vous préférez rester sur place pour affronter l'Homme-Feu, rendez-vous au :"))
    st.page_link("tomes/tome7/page_126.py", label="126", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
