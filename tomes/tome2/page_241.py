import streamlit as st
from combat import combat
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=241, book=2)

fr_text = """
Le silence se fait dans la taverne lorsque l'homme que vous venez
d'accuser se tourne vers vous. « Tu as la langue un peu trop prompte,
étranger, dit-il d'un air menaçant, il serait temps de la couper avant
qu'elle ne t'attire d'autres ennuis. » Il dégaine alors un Poignard à la
lame recourbée et se jette sur vous. La foule des clients forme aussitôt
un cercle autour de vous et il vous est désormais impossible de prendre
la fuite. Il vous faut combattre cet homme jusqu'à la mort de l'un d'entre
vous.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("TRICHEUR", 17, 25)])
    if outcome == "win":
        st.write_stream(stream_text('Si vous êtes vainqueur, rendez-vous au :'))
        st.page_link("tomes/tome2/page_21.py", label="21", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
