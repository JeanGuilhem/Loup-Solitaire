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

check_inventory(current_page_number=221, book=7)

fr_text = """
Une créature, dont l'énorme tête ressemble à celle d'un crapaud,
émerge lentement de l'ombre pour se prélasser dans la lumière
verte qui baigne la plage. Elle vous regarde fixement sans cligner
des yeux, puis se met à ramper dans votre direction. Son corps,
pâle et gonflé comme celui d'un gigantesque ver, est couvert de
plaies béantes, et vous tressaillez à la vue de ce monstre
épouvantable. La créature se redresse en poussant un cri terrible
et s'apprête à vous attaquer avec sa langue aiguisée comme un
rasoir. La rapidité de son attaque ne vous permet pas d'utiliser
un arc.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    invisible = has_magnakai("Invisibilité")
    st.write_stream(stream_text("Vous pouvez fuir le combat après 2 Assauts. Si vous maîtrisez la Discipline Magnakaï de l'Invisibilité, vous pouvez abandonner le combat à tout instant sans perdre de points d'ENDURANCE."))
    outcome = combat([("ZAGOTHAL", 29, 28)], key="zagothal", flee_after=0 if invisible else 2)
    if outcome == "fled":
        rounds = st.session_state["combat_zagothal"]["round"]
        st.write_stream(stream_text("Si vous fuyez le combat après 2 Assauts, rendez-vous au :"))
        st.page_link("tomes/tome7/page_229.py", label="229", icon="📄", disabled=rounds < 2)
        st.write_stream(stream_text("Si vous maîtrisez la Discipline Magnakaï de l'Invisibilité, rendez-vous au :"))
        st.page_link("tomes/tome7/page_70.py", label="70", icon="📄", disabled=not invisible)
    elif outcome == "win":
        st.write_stream(stream_text("Si vous remportez le combat, rendez-vous au :"))
        st.page_link("tomes/tome7/page_271.py", label="271", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
