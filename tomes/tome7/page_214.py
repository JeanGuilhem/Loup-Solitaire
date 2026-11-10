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

check_inventory(current_page_number=214, book=7)

fr_text = """
La porte en fer a plusieurs centimètres d'épaisseur et si vous
voulez la soulever suffisamment haut pour pouvoir vous glisser
en dessous, vous allez devoir produire un effort considérable.
Pour soulever la porte, suivez les règles habituelles de combat
comme si vous étiez désarmé (déduisez 4 points de votre total
d'HABILETÉ). Si vous maîtrisez la Discipline Magnakaï de
Nexus, ne déduisez aucun point de votre total d'HABILETÉ.
Chaque point d'ENDURANCE que vous perdez au cours de ce
combat représente la fatigue due à l'effort que vous devez faire
pour lever la lourde porte.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # « comme si vous étiez désarmé » : -4 et aucune arme ; avec Nexus, l'HABILETÉ de base sans malus.
    # psychic_immune : la Puissance Psychique ne soulève pas une porte.
    nexus = has_magnakai("Nexus")
    outcome = combat(
        [("PORTE DU TUNNEL (Résistance)", 19, 50)],
        unarmed_rounds=1000,
        hability_modifier=4 if nexus else 0,
        psychic_immune=True,
        flee_after=0,
    )
    if outcome == "fled":
        st.write_stream(stream_text("Vous arrêtez l'effort pour aller explorer le tunnel. Rendez-vous au :"))
        st.page_link("tomes/tome7/page_277.py", label="277", icon="📄")
    elif outcome == "win":
        st.write_stream(stream_text("Vous avez réduit la résistance de la porte à zéro. Rendez-vous au :"))
        st.page_link("tomes/tome7/page_114.py", label="114", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
