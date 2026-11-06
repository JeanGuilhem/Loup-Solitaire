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

check_inventory(current_page_number=71, book=6)

fr_text = """
L'homme fait un bond en arrière tout en dégainant une épée à
large lame de sous son manteau en peau d'ours. « Imbécile !
s'écrie-t-il avec mépris. La victoire appartiendra au survivant
! » Vous avez gravement offensé cette brute, et le voilà
maintenant résolu à se battre à mort avec vous - c'est une
question d'honneur. Si vous maîtrisez la Discipline Magnakaï du
Contrôle Animal, ajoutez 2 points à votre total d'HABILETÉ pour
toute la durée de l'affrontement, puisque vous combattez à
cheval.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # à cheval : +2 HABILETÉ avec le Contrôle Animal
    outcome = combat(
        [("BARBENOIRE", 19, 28)],
        hability_modifier=2 if has_magnakai("Contrôle Animal") else 0,
        flee_after=0,
    )
    if outcome == "fled":
        st.write_stream(stream_text("Vous cessez le combat en fuyant au triple galop. Rendez-vous au :"))
        st.page_link("tomes/tome6/page_279.py", label="279", icon="📄")
    if outcome == "win":
        st.write_stream(stream_text("Si vous remportez le combat, rendez-vous au :"))
        st.page_link("tomes/tome6/page_237.py", label="237", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
