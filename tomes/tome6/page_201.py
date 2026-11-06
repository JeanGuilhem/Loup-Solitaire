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

check_inventory(current_page_number=201, book=6)

fr_text = """
Le sergent ordonne à ses hommes de reculer - il est persuadé de
pouvoir vous battre seul, sans aide, afin de montrer ses talents de
soldat. Sûr de lui, il sourit déjà à son futur triomphe et lève sa
lance et son bouclier. Vous pouvez vous battre avec n'importe
quelle arme, excepté un Arc.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # l'Arc ne compte pas au corps à corps : le moteur l'écarte de lui-même
    outcome = combat([("SERGENT DE VILLE", 18, 27)], max_rounds=3)
    if outcome == "win":
        st.write_stream(stream_text("Si vous l'emportez et que le combat dure 3 Assauts au plus, rendez-vous au :"))
        st.page_link("tomes/tome6/page_15.py", label="15", icon="📄")
    elif outcome == "rounds_over":
        st.write_stream(stream_text("Si le combat dure plus de 3 Assauts, rendez-vous au :"))
        st.page_link("tomes/tome6/page_87.py", label="87", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
