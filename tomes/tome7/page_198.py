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

check_inventory(current_page_number=198, book=7)

fr_text = """
Soudain, vous comprenez la terrible intention de la main. C'est
un prédateur, une entité malfaisante qui ne peut survivre qu'en
consommant une seule sorte de nourriture : le cerveau humain
vivant ! Vous plongez, puis vous roulez au sol pour éviter la
première attaque. Vous vous en sortez avec quelques
égratignures à la tête (vous perdez 2 points d'ENDURANCE),
mais la main s'élève à nouveau, et vous craignez que votre vie ne
s'achève là. Cette créature est immunisée contre la Puissance
Psychique mais pas contre le Foudroiement Psychique.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-2)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-2)

    outcome = combat([("MAIN COUPÉE", 18, 30)], psychic_power_immune=True)
    if outcome == "win":
        st.write_stream(stream_text("Si vous remportez le combat, rendez-vous au :"))
        st.page_link("tomes/tome7/page_22.py", label="22", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
