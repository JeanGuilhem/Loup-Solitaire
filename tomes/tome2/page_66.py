import streamlit as st
from combat import combat
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=66, book=2)

fr_text = """
Lorsque vous levez la lame étincelante de votre glaive le CAPITAINE
ZOMBIE tire de sa veste en lambeaux un poignard menaçant. Il vous
faut le combattre jusqu'à la mort de l'un de vous deux.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(
        stream_text(
            "La puissance du Glaive de Sommer vous permet de multiplier par 2 tous les points d'ENDURANCE "
            "que le capitaine perdra au cours de l'affrontement, mais votre adversaire est insensible à la "
            "Discipline Kaï de la Puissance Psychique."
        )
    )
    outcome = combat([("CAPITAINE ZOMBIE", 15, 15)], psychic_immune=True, undead=True)
    if outcome == "win":
        st.write_stream(stream_text("Si vous êtes vainqueur, rendez-vous au :"))
        st.page_link("tomes/tome2/page_218.py", label="218", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
