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

check_inventory(current_page_number=260, book=4)

fr_text = """
Les Chiens de Guerre s'élancent en direction de la barricade les
yeux brillants de férocité. Cinq de ces molosses ouvrent une
brèche dans la barrière en renversant sacs et tonneaux, et se
jettent sur les soldats qui vous entourent. D'un seul coup de votre
arme, vous tuez deux de ces Chiens répugnants mais, dans le feu
de l'action, vous ne remarquez pas que d'autres molosses
bondissent sur vous par-derrière. Sous le choc vous êtes précipité
en avant sur les débris de la barricade effondrée. Avant que vous
ayez pu vous relever, ils vous plantent les crocs dans les jambes.
Vous devez à présent les combattre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("CHIENS DE GUERRE VASSAGONIENS", 18, 30)], max_rounds=3)
    if outcome in ("win", "rounds_over"):
        st.write_stream(stream_text('Si vous êtes toujours vivant après 3 Assauts, rendez-vous au :'))
        st.page_link("tomes/tome4/page_311.py", label="311", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
