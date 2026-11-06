import streamlit as st
from combat import combat
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_magnakai,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=254, book=6)

fr_text = """
Vous traversez le pont en courant puis vous descendez les marches
qui mènent à l'entrepont. Mais vos pieds ont à peine touché les
planches maculées de sang que vous êtes attaqué par-derrière par
deux pirates. A moins que vous ne possédiez la Discipline Magnakaï
de l'Art de la Chasse, ôtez 2 points à votre total d'HABILETÉ pour
le premier Assaut du combat.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat(
        [("PIRATES", 18, 27)],
        first_round_modifier=0 if has_magnakai("Art de la Chasse") else -2,
    )
    if outcome == "win":
        st.write_stream(stream_text("Si vous sortez vainqueur de la bataille, rendez-vous au :"))
        st.page_link("tomes/tome6/page_77.py", label="77", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
