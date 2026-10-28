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

check_inventory(current_page_number=110, book=3)

fr_text = """
La porte de pierre s'ouvre en grinçant sur une petite salle
faiblement éclairée. Un monolithe noir de 2,50 mètres environ se
dresse devant vous. Il est couvert d'étranges symboles gravés à sa
surface. Vous vous en approchez pour l'examiner de plus près
lorsque, soudain, la porte commence à se refermer derrière vous.
Or, il n'y a pas de levier de ce côté-ci du mur.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez vous ruer sur la porte pour tenter de passer par l'entrebâillement, rendez-vous au :"))
    st.page_link("tomes/tome3/page_283.py", label="283", icon="📄")
    st.write_stream(stream_text("Si vous préférez rester où vous êtes, rendez-vous au :"))
    st.page_link("tomes/tome3/page_256.py", label="256", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
