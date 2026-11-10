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

check_inventory(current_page_number=126, book=7)

fr_text = """
En poussant un cri à faire frémir, votre adversaire vous saute à la
gorge. Cette créature est insensible à la Puissance Psychique,
mais non au Foudroiement Psychique. Par ailleurs, à moins que
vous ne maîtrisiez la Discipline Magnakaï de Nexus, vous devrez
doubler tous les points d'ENDURANCE que vous perdrez
éventuellement lors de ce combat, à cause des graves brûlures
que vous subirez.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # sans Nexus, les brûlures doublent vos pertes d'ENDURANCE
    outcome = combat([("HOMME-FEU", 14, 40)], psychic_power_immune=True,
                     ls_loss_multiplier=1 if has_magnakai("Nexus") else 2)
    if outcome == "win":
        st.write_stream(stream_text("Si vous sortez vainqueur de cet affrontement, rendez-vous au :"))
        st.page_link("tomes/tome7/page_147.py", label="147", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
