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

check_inventory(current_page_number=193, book=4)

fr_text = """
Hurlant et grognant, les Chiens de Guerre bondissent sur la
barricade, leurs yeux grands ouverts lançant des éclats écarlates
dans le feu de la bataille. Piétinant les corps des morts et des
mourants, ils se ruent sur les défenseurs sommerlundais. Tout
autour de vous, des soldats sont projetés à terre par les molosses
impitoyables. Vous faites un pas en arrière au moment où un
Chien hurlant renverse la barrière de sacs et de tonneaux. Mais
avant qu'il ait pu vous atteindre, vous lui fracassez la tête avec
votre arme. Un autre Chien de Guerre vous attaque par-derrière
et vous jette contre la barricade effondrée. Avant que vous n'ayez
pu vous dégager, deux autres molosses plantent leurs crocs dans
votre jambe. Il vous faut à présent livrer un combat sans merci.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("CHIENS DE GUERRE", 17, 30)], max_rounds=2)
    if outcome in ("win", "rounds_over"):
        st.write_stream(stream_text('Si vous êtes toujours vivant après avoir mené 2 Assauts, rendez-vous au :'))
        st.page_link("tomes/tome4/page_311.py", label="311", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
