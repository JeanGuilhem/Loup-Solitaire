import streamlit as st
from combat import combat
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=270, book=2)

fr_text = """
GANON bondit de sa chaise et tire son épée. Un instant plus tard, son
frère DORIER est à son côté. Il vous faut les combattre tous deux en les
considérant comme un seul et même ennemi.
La soudaineté de votre attaque vous permet d'ajouter 2 points à votre
total d'HABILETÉ, mais lors du premier assaut seulement. Sachez
également qu'en raison de la force exceptionnelle de leur volonté, ils
sont insensibles à la Discipline Kaï de la Puissance Psychique.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("GANON et DORIER", 28, 30)], first_round_modifier=2, psychic_immune=True)
    if outcome == "win":
        st.write_stream(stream_text("Si vous sortez vainqueur de ce combat, rendez-vous au :"))
        st.page_link("tomes/tome2/page_33.py", label="33", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
