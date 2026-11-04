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

check_inventory(current_page_number=223, book=5)

fr_text = """
Brusquement, la douleur cesse mais le combat ne fait que
commencer. Un nuage noir comme la mort s'échappe de la
bouche de Haakon, descend le long de son bras et vient se nicher
dans le creux de sa main. Un tourbillon très sombre se forme
lentement et bientôt des ailes et des tentacules se déploient de
toutes parts. Haakon lance alors une malédiction qui fait
trembler les murs du Tombeau, tandis qu'un flot d'horreur
mortel coule de sa main.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("CRÉATURE DE LA CRYPTE", 24, 40)])
    if outcome == "win":
        st.write_stream(stream_text("Si vous gagnez ce combat, rendez-vous au :"))
        st.page_link("tomes/tome5/page_353.py", label="353", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
