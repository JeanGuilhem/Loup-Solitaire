import streamlit as st
from combat import combat
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=194, book=5)

fr_text = """
Le Yas est un serpent constricteur. Il tue ses proies en les
étouffant grâce aux anneaux puissants de son long corps. Ses
yeux endormis sont maintenant grands ouverts, les pupilles sont
verticales et l'iris d'un rouge vif. Il vous fixe d'un regard
envoûtant et vous comprenez avec horreur qu'il essaie de vous
hypnotiser.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("A moins que vous ne maîtrisiez la Discipline Kaï du Bouclier Psychique, déduisez 3 points de votre total d'HABILETÉ pour toute la durée du combat."))
    outcome = combat([("YAS", 14, 28)], hability_modifier=0 if has_kai("Bouclier psychique") else -3)
    if outcome == "win":
        st.write_stream(stream_text('Si vous remportez le combat, rendez-vous au :'))
        st.page_link("tomes/tome5/page_35.py", label="35", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
