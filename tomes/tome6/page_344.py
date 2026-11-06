import streamlit as st
from combat import combat
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

# Le moteur ne sait pas arrêter un combat quand l'ennemi tombe à N points : on fait combattre
# les 25 points à retirer (50 -> 25), d'où une ENDURANCE affichée de 25.
# Venu du 209, le Loup Solitaire a abandonné son Arc et combat à mains nues.

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=344, book=6)

fr_text = """
L'affreuse créature se jette sur vous !

**DAKOMYD** — HABILETÉ : 25 — ENDURANCE : 50

Cet animal est insensible à la Puissance Psychique comme au
Foudroiement Psychique.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        st.session_state.visibility_from_209 = st.session_state.last_page_number == 209
    unarmed = 50 if st.session_state.get("visibility_from_209") else 0
    if unarmed:
        st.write("*Vous combattez à mains nues.*")
    outcome = combat([("DAKOMYD", 25, 50)], psychic_immune=True, unarmed_rounds=unarmed, enemy_stop_at=25)
    if outcome == "win":
        st.write_stream(stream_text("Si vous réduisez son total d'ENDURANCE à 25 ou moins, cessez le combat et rendez-vous au :"))
        st.page_link("tomes/tome6/page_310.py", label="310", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
