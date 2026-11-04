import streamlit as st
from combat import combat
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=393, book=5)

fr_text = """
Vous courez tête baissée à travers le feuillage, le cri perçant du
Vordak résonnant à vos oreilles. A moins que vous ne maîtrisiez
la Discipline Kaï du Bouclier Psychique, vous perdez 2 points d'ENDURANCE. Brusquement, un Drakkar surgit des arbres devant vous, son
épée noire levée haut au-dessus de sa tête et prêt à vous asséner
un coup mortel.
Pour le premier Assaut, diminuez votre total d'HABILETÉ de 2
points en raison de l'effet de surprise provoqué par l'attaque du
Drakkar. Vous pourrez fuir le combat après 3 Assauts.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if not has_kai("Le Bouclier Psychique"):
        if is_new_page():
            change_endurance(-2)
        st.metric(label="Endurance", value=st.session_state.endurance, delta=-2)
    outcome = combat([("DRAKKAR", 16, 25)], first_round_modifier=-2, flee_after=3)
    if outcome == "fled":
        st.write_stream(stream_text("Si vous souhaitez fuir le combat, rendez-vous au :"))
        st.page_link("tomes/tome5/page_228.py", label="228", icon="📄")
    elif outcome == "win":
        st.write_stream(stream_text("Si vous sortez vainqueur, rendez-vous au :"))
        st.page_link("tomes/tome5/page_255.py", label="255", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
