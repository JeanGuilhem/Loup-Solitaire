import streamlit as st
from combat import combat
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=159, book=5)

fr_text = """
Vous parvenez à enfoncer la porte mais, emporté par votre élan,
vous ne pouvez pas vous arrêter. Vous dégringolez les marches la
tête la première, et vous atterrissez en boule sur le sol de marbre
d'une antichambre, à quelques centimètres d'un soldat armé qui
garde les portes de l'Armurerie du Palais. (Vous perdez 2 points
d'ENDURANCE.) Il est surpris par votre entrée originale, mais il
retrouve rapidement tous ses esprits et passe à l'attaque.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-2)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-2)

    st.write_stream(stream_text("Ôtez 2 points à votre total d'HABILETÉ pour les 3 premiers Assauts, car vous êtes allongé sur le sol. Vous n'avez pas la possibilité de fuir et vous devez combattre le Garde jusqu'à la mort."))
    outcome = combat([("GARDE DE L'ARMURERIE", 16, 22)], first_round_modifier=-2, first_rounds=3)
    if outcome == "win":
        st.write_stream(stream_text('Si vous êtes vainqueur, rendez-vous au :'))
        st.page_link("tomes/tome5/page_52.py", label="52", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
