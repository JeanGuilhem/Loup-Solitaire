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

check_inventory(current_page_number=36, book=7)

fr_text = """
Par une ouverture pratiquée dans le mur de droite, vous
apercevez un escalier en colimaçon qui résonne de bruits de pas.
A en juger par le vacarme, vous estimez qu'une bonne demi-douzaine de gardes en armure sont en train de descendre
l'escalier. Ils atteindront le palier où vous vous trouvez d'une
minute à l'autre... Qu'allez-vous faire ?
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous voulez attendre les gardes de pied ferme et vous préparer à combattre, rendez-vous au :'))
    st.page_link("tomes/tome7/page_273.py", label="273", icon="📄")

    st.write_stream(stream_text("Si vous préférez descendre l'escalier avant qu'ils vous rattrapent, rendez-vous au :"))
    st.page_link("tomes/tome7/page_55.py", label="55", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
