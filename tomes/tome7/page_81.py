import streamlit as st
from combat import combat
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

check_inventory(current_page_number=81, book=7)

fr_text = """
La rapidité de votre attaque surprend complètement votre
ennemi. Il tente de parer votre coup de poing en se protégeant
avec son arbalète, mais vous la lui faites sauter des mains, le
laissant tremblant et désarmé face à vous.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("GARDE DE LA SALLE DU TRÔNE", 14, 22)])
    if outcome == "win":
        st.write_stream(stream_text("Si vous sortez vainqueur du combat, rendez-vous au :"))
        st.page_link("tomes/tome7/page_105.py", label="105", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
