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

check_inventory(current_page_number=281, book=4)

fr_text = """
La créature disparaît et vous vous retrouvez allongé par terre
dans le tunnel. Vous avez le souffle court, votre cœur bat avec
force et une sueur froide ruisselle sur votre corps. Vous
comprenez alors ce qui vous est arrivé. Les spores des
champignons ont provoqué en vous une hallucination. Le Démon
des Tunnels n'existait que dans votre esprit. Malheureusement,
bien qu'il ne se soit agi là que d'une illusion, vous avez bel et bien
perdu les points d'ENDURANCE que vous a coûtés ce combat
imaginaire. Vous vous êtes en effet infligé des blessures à vous-
même en vous jetant contre les murs aux aspérités pointues.
Tandis que les effets de ces spores malfaisantes disparaissent peu
à peu, une fatigue irrépressible vous submerge et vous perdez
conscience. Vous ne vous réveillez qu'au bout de plusieurs
heures, la gorge et la tête douloureuses. Vous allumez à nouveau
votre Torche et vous reprenez votre chemin le long du tunnel.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome4/page_185.py", label="185", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
