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

check_inventory(current_page_number=235, book=7)

fr_text = """
La main est rapide, mais vous l'êtes plus encore. Vous évitez sa
première attaque en roulant au sol, puis vous vous ramassez sur
vous-même, prêt à parer sa prochaine attaque. La main s'élève à
nouveau, et vous comprenez tout à coup, en observant sa forme
effrayante, quelles sont ses terribles intentions. Cette main est un
prédateur, une entité malfaisante qui ne peut vivre qu'en
consommant une seule sorte de nourriture : le cerveau humain
vivant ! Vous combattez la peur que vous sentez monter en vous
tandis que la main se rapproche à grande vitesse. Cette créature
est immunisée contre la Puissance Psychique mais pas contre le
Foudroiement Psychique.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("MAIN COUPÉE", 18, 30)], psychic_power_immune=True)
    if outcome == "win":
        st.write_stream(stream_text("Si vous remportez le combat, rendez-vous au :"))
        st.page_link("tomes/tome7/page_22.py", label="22", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
