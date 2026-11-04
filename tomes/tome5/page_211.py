import streamlit as st
from inventory import (
    buy_button,
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

check_inventory(current_page_number=211, book=5)

fr_text = """
Malgré vos craintes, le vin vert s'avère délicieux. Une douce
chaleur monte lentement en vous, vous remplissant d'une
agréable sensation de bien-être. Vous gagnez 2 points
d'ENDURANCE. L'homme a l'air ravi de votre réaction et il vous
propose de vous en vendre une bouteille pour 5 Pièces d'Or.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(2)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=2)

    st.write_stream(stream_text("Si vous voulez acheter une bouteille de Kourshah, payez les 5 Pièces d'Or. (Il y a suffisamment de Kourshah dans la bouteille pour vous faire regagner 4 points d'ENDURANCE.)"))
    buy_button("KOURSHAH", 5, key="kourshah", label="Acheter une bouteille de Kourshah (5 Couronnes)")

    st.write_stream(stream_text("Si vous voulez à présent le questionner sur Tipasa le Vagabond, rendez-vous au :"))
    st.page_link("tomes/tome5/page_318.py", label="318", icon="📄")

    st.write_stream(stream_text("Si vous préférez poursuivre votre route vers Ikaresh, sans rien lui demander, rendez-vous au :"))
    st.page_link("tomes/tome5/page_272.py", label="272", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
