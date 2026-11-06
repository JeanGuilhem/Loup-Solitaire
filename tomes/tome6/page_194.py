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

check_inventory(current_page_number=194, book=6)

fr_text = """
La meute hurlante se jette sur vous en poussant des cris de
forcenés. Ils tailladent violemment vos jambes nues et tentent de
vous désarçonner. Si vous maîtrisez la Discipline Magnakaï du
Contrôle Animal, vous pouvez ajouter 2 points à votre total
d'HABILETÉ pour la durée du combat, car la maîtrise de cette
Discipline vous permet d'ordonner à votre cheval d'attaquer avec
ses sabots.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("DISCIPLES DE VASHNA", 22, 48)], hability_modifier=2 if has_magnakai("Contrôle Animal") else 0,
                     flee_after=0)
    if outcome == "fled":
        st.write_stream(stream_text("Vous abandonnez le combat ; rendez-vous au :"))
        st.page_link("tomes/tome6/page_289.py", label="289", icon="📄")
    elif outcome == "win":
        st.write_stream(stream_text("Si vous sortez vainqueur du combat, rendez-vous au :"))
        st.page_link("tomes/tome6/page_145.py", label="145", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
