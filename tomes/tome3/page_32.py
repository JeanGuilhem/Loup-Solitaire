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

check_inventory(current_page_number=32, book=3)

fr_text = """
Les créatures surgissent de la chute d'eau et bondissent sur vous ;
il vous faut les combattre une par une.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat(
        [("Premier LANGUABARB", 11, 35), ("Deuxième LANGUABARB", 10, 32), ("Troisième LANGUABARB", 8, 30)],
        stop_when_wounded=True,
    )
    if outcome == "wounded":
        st.write_stream(
            stream_text(
                "Si vous perdez des points d'ENDURANCE au cours de ce combat, rendez-vous immédiatement "
                'au :'
            )
        )
        st.page_link("tomes/tome3/page_66.py", label="66", icon="📄")
    elif outcome == "win":
        st.write_stream(
            stream_text(
                "Si vous remportez le combat sans perdre de points d'ENDURANCE, rendez-vous au :"
            )
        )
        st.page_link("tomes/tome3/page_25.py", label="25", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
