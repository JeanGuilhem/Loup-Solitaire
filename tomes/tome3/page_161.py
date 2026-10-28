import streamlit as st
from combat import combat
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

check_inventory(current_page_number=161, book=3)

fr_text = """
Le Barbare des Glaces s'avance lentement et ses yeux blancs
dépourvus de pupilles vous donnent la chair de poule. Dans sa
main droite, il tient un cimeterre en os, mais, bien qu'il soit prêt
à frapper, ses gestes sont raides et incertains, comme s'il vous
attaquait contre sa volonté. Le Barbare est insensible à la
Discipline Kaï de la Puissance Psychique.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("BARBARE DES GLACES", 17, 29)], psychic_immune=True)
    if outcome == "win":
        st.write_stream(stream_text('Si vous sortez vainqueur de ce combat, rendez-vous au :'))
        st.page_link("tomes/tome3/page_210.py", label="210", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
