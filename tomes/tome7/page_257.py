import streamlit as st
from combat import combat
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    has_magnakai,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=257, book=7)

fr_text = """
Un autre claquement déchire l'air, et le fouet invisible vous
atteint en travers de la cuisse qu'il marque d'une estafilade
violette. (Vous perdez 2 points d'ENDURANCE). Vous vous
efforcez de localiser votre ennemi à l'aide de vos sens Kaï, mais la
magie qui le protège est beaucoup trop forte. Si vous ne maîtrisez
pas la Discipline Magnakaï de l'Art de la Chasse, réduisez de 2
points votre total d'HABILETÉ pour toute la durée du combat. Si
vous possédez une Couverture ou un Habit Rouge, vous pouvez
l'enrouler autour de votre bras comme protection
supplémentaire contre les coups de votre ennemi (dans ce cas,
votre total d'HABILETÉ augmente de 1 point).
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-2)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-2)

    modifier = (0 if has_magnakai("Art de la Chasse") else -2) + (
        1 if has_item("COUVERTURE") or has_item("HABIT ROUGE") else 0
    )
    st.write_stream(stream_text("Vous pouvez fuir le combat après 3 Assauts en remontant le tunnel."))
    outcome = combat([("FOUET INVISIBLE", 24, 26)], hability_modifier=modifier, flee_after=3)
    if outcome == "fled":
        st.write_stream(stream_text("Vous remontez le tunnel en fuyant : rendez-vous au :"))
        st.page_link("tomes/tome7/page_64.py", label="64", icon="📄")
    elif outcome == "win":
        st.write_stream(stream_text("Si vous remportez le combat, rendez-vous au :"))
        st.page_link("tomes/tome7/page_186.py", label="186", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
