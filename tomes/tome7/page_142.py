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

check_inventory(current_page_number=142, book=7)

fr_text = """
Au bout du couloir délimitant le quartier des cellules, un escalier
descend vers un niveau inférieur. Cependant, l'entrée est gardée
par une créature à l'air féroce, munie d'une grande hache.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("GEÔLIER RAKHOS", 17, 22)], max_rounds=3)
    if outcome == "win":
        st.write_stream(stream_text("Si vous remportez le combat en trois Assauts ou moins, rendez-vous au :"))
        st.page_link("tomes/tome7/page_238.py", label="238", icon="📄")
    elif outcome == "rounds_over":
        # le Geôlier n'est pas encore mort : le combat continue jusqu'au bout (le §212 suppose sa mort)
        st.caption("Le combat dure plus de trois Assauts : achevez votre adversaire.")
        remaining = st.session_state["combat_combat"]["enemy_endurance"]
        end = combat([("GEÔLIER RAKHOS", 17, remaining)], key="suite")
        if end == "win":
            st.write_stream(stream_text("Si le combat dure plus de trois Assauts, rendez-vous au :"))
            st.page_link("tomes/tome7/page_212.py", label="212", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
