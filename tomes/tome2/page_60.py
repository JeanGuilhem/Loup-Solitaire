import streamlit as st
from combat import combat
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=60, book=2)

fr_text = """
HALVORC vous contemple d'un air stupéfait et incrédule.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(
        stream_text(
            "Il est incapable de se défendre au cours des deux premiers assauts en raison de l'effet de "
            "surprise de votre attaque. Vous ne perdrez donc aucun point d'ENDURANCE lors de ces deux assauts."
        )
    )
    st.write_stream(
        stream_text(
            "Si votre adversaire est toujours en vie au moment du troisième assaut, il s'élancera sur vous "
            "armé d'un Poignard."
        )
    )
    outcome = combat([("HALVORC", 8, 11)], ls_immune_rounds=2)
    if outcome == "win":
        st.write_stream(stream_text("Si vous sortez vainqueur du combat, rendez-vous au :"))
        st.page_link("tomes/tome2/page_76.py", label="76", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
