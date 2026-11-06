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

check_inventory(current_page_number=283, book=6)

fr_text = """
Grâce à votre pouvoir Magnakaï, vous pouvez suivre très
précisément la trajectoire de la flèche mortelle qui fend l'air en
sifflant vers votre poitrine. Tout semble se dérouler au ralenti.
Vous déviez la flèche de sa trajectoire en la frappant à la
pointe. Votre adversaire jette aussitôt son arbalète par terre, et
vous l'entendez crier derrière son casque noir : « Meurs, homme du
Nord ! » Le guerrier franchit la porte de Denka, puis il vous
charge en brandissant une hache dans sa main gantée. Vous ne
pouvez pas éviter l'affrontement et vous devez le combattre
jusqu'à la mort. Étant donné la vitesse de l'attaque, vous ne
pouvez pas utiliser d'Arc. Si vous maîtrisez la Discipline
Magnakaï du Contrôle Animal, votre total d'HABILETÉ est augmenté
de 1 point pour toute la durée du combat.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # pas d'Arc possible : le moteur ne compte de toute façon pas l'Arc au corps à corps
    outcome = combat(
        [("ASSASSIN À L'ARMURE", 24, 26)],
        hability_modifier=1 if has_magnakai("Contrôle Animal") else 0,
    )
    if outcome == "win":
        st.write_stream(stream_text("Si vous êtes vainqueur, rendez-vous au :"))
        st.page_link("tomes/tome6/page_28.py", label="28", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
