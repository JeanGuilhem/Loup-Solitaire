import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=185, book=7)

fr_text = """
Un martèlement sec, tel celui des sabots d'un cheval claquant sur
des pavés vous arrête brusquement. Votre instinct Kaï vous
avertit que d'autres créatures malfaisantes se sont lancées à votre
poursuite dans le tunnel : continuer à avancer dans cette
direction serait suicidaire. Vous avez encore deux cents mètres à
parcourir le long de l'étroit passage avant d'arriver au tunnel
opposé. Vous faites demi-tour et vous vous mettez à courir en
priant que les Dhax ne vous rejoignent pas avant que vous ayez
atteint l'entrée.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    roll = hazard_roll(key="dhax")
    if roll is not None:
        st.write_stream(stream_text("Si le chiffre tiré est compris entre 0 et 8, rendez-vous au :"))
        st.page_link("tomes/tome7/page_241.py", label="241", icon="📄", disabled=roll > 8)
        st.write_stream(stream_text("Si vous avez tiré un 9, rendez-vous au :"))
        st.page_link("tomes/tome7/page_106.py", label="106", icon="📄", disabled=roll != 9)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
