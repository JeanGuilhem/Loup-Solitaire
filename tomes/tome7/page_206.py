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

check_inventory(current_page_number=206, book=7)

fr_text = """
Vous visez et vous tirez une fraction de seconde plus tard. Vous
atteignez le chef en pleine poitrine, ce dernier trébuche en
arrière, déséquilibré par la force d'impact de votre flèche. Ses
compagnons se mettent alors à pousser des cris de colère et se
précipitent sur vous en brandissant de longs couteaux et des
haches pour venger leur chef.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("RAKHOS DE ZAHDA", 28, 35)], key="rakhos")
    if outcome == "win":
        rounds = st.session_state["combat_rakhos"]["round"]
        st.write_stream(stream_text("Si vous remportez le combat en 3 Assauts ou moins, rendez-vous au :"))
        st.page_link("tomes/tome7/page_17.py", label="17", icon="📄", disabled=rounds > 3)
        st.write_stream(stream_text("Si le combat dure plus de 3 Assauts, rendez-vous au :"))
        st.page_link("tomes/tome7/page_160.py", label="160", icon="📄", disabled=rounds <= 3)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
