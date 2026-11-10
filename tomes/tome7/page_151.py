import streamlit as st
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

check_inventory(current_page_number=151, book=7)

fr_text = """
Vous vous frayez un chemin parmi les bulles aussi facilement que
si vous tranchiez des toiles d'araignée. A chaque fois que votre
épée perce leur membrane gélatineuse, elles explosent
bruyamment et tombent en lambeaux sur le sol. Vous continuez
à avancer, guettant le moindre signe de danger. Soudain, une
grande ombre projetée sur le sol, non loin de vous, vous met en
alerte. Mais vos craintes se muent en désarroi quand vous
découvrez que l'ombre est, en fait, un gouffre noir et profond,
déchirant le passage sur une dizaine de mètres, et n'offrant
aucun moyen de le franchir. Au-dessus de vous, l'éclaircissement
soudain de la brume annonce le retour inopiné du crâne :

*Le moyen de traverser défie votre regard ;*

*Trouvez-le, ou bien restez et battez-vous !*
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    psychic_or_intuition = has_magnakai("Écran Psychique") or has_magnakai("Intuition")
    st.write_stream(stream_text("Si vous maîtrisez la Discipline Magnakaï de l'Écran Psychique ou de l'Intuition, rendez-vous au :"))
    st.page_link("tomes/tome7/page_39.py", label="39", icon="📄", disabled=not psychic_or_intuition)

    st.write_stream(stream_text("Si vous ne maîtrisez ni l'une ni l'autre de ces Disciplines, rendez-vous au :"))
    st.page_link("tomes/tome7/page_261.py", label="261", icon="📄", disabled=psychic_or_intuition)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
