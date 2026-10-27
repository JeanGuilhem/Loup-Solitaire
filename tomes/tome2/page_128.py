import streamlit as st
from combat import combat
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=128, book=2)

fr_text = """
Une lueur dorée parcourt la lame du Glaive lorsque vous le levez au-
dessus de votre tête pour faire face à l'ennemi. Vous êtes attaqué par six
ZOMBIES terrifiants que vous devez combattre en les considérant
comme un seul et même adversaire.
Ce sont des morts vivants et la puissance du Glaive de Sommer vous
permet donc de multiplier par deux tous les points d'ENDURANCE
qu'ils perdront au cours du combat. Ils restent cependant insensibles à
la Discipline Kaï de la Puissance Psychique.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("LES ZOMBIES", 13, 19)], psychic_immune=True, undead=True)
    if outcome == "win":
        st.write_stream(stream_text("Vous êtes vainqueur, rendez-vous au :"))
        st.page_link("tomes/tome2/page_237.py", label="237", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
