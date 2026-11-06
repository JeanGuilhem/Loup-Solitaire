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

# La fuite au galop se choisit avant le combat : le lien 191 est grisé une fois le combat engagé.

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=337, book=6)

fr_text = """
Tout à coup, une douzaine de brigands à la mine patibulaire
franchissent le mur du cimetière. Malgré ses blessures, l'homme
se raidit et dégaine un vieux cimeterre rouillé en poussant un
petit cri rauque entre ses dents noires. Il donne le signal de
l'attaque, et toute la bande se précipite sur vous en brandissant
des armes ébréchées au-dessus de leurs têtes.

**PILLEURS DE TOMBE** — HABILETÉ : 17 — ENDURANCE : 32
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    started = st.session_state.get("combat_combat", {}).get("status", "setup") != "setup"
    st.write_stream(stream_text("Si vous souhaitez prendre la fuite au galop vers l'ouest, rendez-vous au :"))
    st.page_link("tomes/tome6/page_191.py", label="191", icon="📄", disabled=started)

    st.write_stream(stream_text('Si vous préférez tenir tête :'))
    outcome = combat([("PILLEURS DE TOMBE", 17, 32)])
    if outcome == "win":
        st.write_stream(stream_text('Si vous remportez le combat, rendez-vous au :'))
        st.page_link("tomes/tome6/page_40.py", label="40", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
