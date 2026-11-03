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

check_inventory(current_page_number=147, book=4)

fr_text = """
Le Garde vous entend approcher et fait aussitôt volte-face. Il
vous regarde d'un air stupéfait puis tire son épée. La surprise de
votre attaque vous donne un avantage au cours du premier
Assaut. De ce fait, vous ne perdrez aucun point d'ENDURANCE,
quelles que soient les indications données par la Table des Coups
Portés. A partir du deuxième Assaut, le combat se poursuivra
normalement.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("GARDE DU PONT", 14, 23)], ls_immune_rounds=1)
    if outcome == "win":
        st.write_stream(stream_text('Si vous remportez la victoire, rendez-vous au :'))
        st.page_link("tomes/tome4/page_280.py", label="280", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
