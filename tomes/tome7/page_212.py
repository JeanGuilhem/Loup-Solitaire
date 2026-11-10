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

check_inventory(current_page_number=212, book=7)

fr_text = """
Tandis que l'Homme-Bête s'affale sur le sol, deux autres gardiens
surgissent dans le couloir en poussant des hurlements de colère à
la vue du corps de leur compagnon d'armes. Ils se jettent sur
vous dans une furieuse attaque.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("PREMIER GEÔLIER-RAKHOS", 17, 23), ("SECOND GEÔLIER-RAKHOS", 16, 21)])
    if outcome == "win":
        st.write_stream(stream_text("Si vous remportez le combat, rendez-vous au :"))
        st.page_link("tomes/tome7/page_80.py", label="80", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
