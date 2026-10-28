import streamlit as st
from combat import combat
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=260, book=3)

fr_text = """
La surprise de votre attaque vous permet de frapper par deux fois
le Barbare des Glaces avant qu'il ait eu le temps de réagir. Vous
ne perdrez donc aucun point d'ENDURANCE au cours des deux
premiers Assauts de ce combat, quelles que soient les indications
qui vous seront données par la Table des Coups Portés. Le
Barbare, en revanche, perdra les points d'ENDURANCE indiqués
par cette même Table. Si, lors du troisième Assaut, votre
adversaire est toujours vivant, il dégainera une épée en os et vous
attaquera à son tour. Le combat se déroulera alors à la manière
habituelle. Ce Barbare, notez-le, est invulnérable à la Discipline
Kaï de la Puissance Psychique.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("BARBARE DES GLACES", 17, 29)], psychic_immune=True, ls_immune_rounds=2)
    if outcome == "win":
        st.write_stream(stream_text('Si vous remportez la victoire, rendez-vous au :'))
        st.page_link("tomes/tome3/page_210.py", label="210", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
