import streamlit as st
from combat import combat
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=176, book=4)

fr_text = """
Dans un grand fracas, votre cheval heurte violemment le flanc de
l'étalon d'un des brigands et vous êtes projeté à terre. A moitié
assommé par le choc, vous ne parvenez pas à esquiver le coup
que vous porte l'un des Guerriers ennemis. Une lame vous blesse
à l'épaule et vous perdez 3 points d'ENDURANCE. Vous vous
relevez aussitôt pour affronter votre agresseur ; il vous est
impossible de prendre la fuite et il vous faut combattre jusqu'à la
mort.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-3)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-3)

    outcome = combat([("GUERRIER PILLARD", 17, 25)])
    if outcome == "win":
        st.write_stream(stream_text('Si vous êtes vainqueur, rendez-vous au :'))
        st.page_link("tomes/tome4/page_7.py", label="7", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
