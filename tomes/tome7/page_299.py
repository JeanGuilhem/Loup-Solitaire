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

check_inventory(current_page_number=299, book=7)

fr_text = """
Tandis que vous tirez votre arme pour affronter l'ennemi, le
guerrier court se mettre à l'abri. « Pauvre idiot ! » crie-t-il en se
retournant avant de disparaître dans le tunnel. Les créatures
s'avancent en poussant des gémissements de délectation, tels des
prédateurs cruels et affamés s'apprêtant à se repaître de leurs
proies. Des griffes jaillissent à l'extrémité de leurs doigts palmés
et leurs yeux se mettent à briller d'une féroce lueur rouge au
moment où elles se jettent sur vous.
Il y a un piège juste derrière vous et vous ne pouvez pas fuir :
vous devez combattre les Dhax jusqu'à la mort.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("DHAX", 27, 35)])
    if outcome == "win":
        st.write_stream(stream_text("Si vous remportez le combat, rendez-vous au :"))
        st.page_link("tomes/tome7/page_339.py", label="339", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
