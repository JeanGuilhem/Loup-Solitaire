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

check_inventory(current_page_number=19, book=7)

fr_text = """
Une ombre passe devant vous et vous relâchez la corde de votre
arc. Hélas ! votre flèche manque sa cible, et vous entendez, en
guise d'avertissement, un hurlement fantomatique avant d'être
assailli par les créatures qui surgissent de la fumée tourbillonnante et tentent de vous donner de grands coups de
griffes et de dents.
A moins que vous ne maîtrisiez la Discipline Magnakaï de l'Art
de la Chasse, déduisez 3 points de votre total d'HABILETÉ
durant les 2 premiers Assauts, cela en raison de la rapidité
d'attaque de vos ennemis.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat(
        [("DHAX", 25, 32)],
        first_round_modifier=0 if has_magnakai("Art de la Chasse") else -3,
        first_rounds=2,
        flee_after=3,
    )
    if outcome == "fled":
        st.write_stream(stream_text("Vous fuyez le combat en vous échappant par le passage voûté qui se trouve à l'opposé. Rendez-vous au :"))
        st.page_link("tomes/tome7/page_241.py", label="241", icon="📄")
    elif outcome == "win":
        st.write_stream(stream_text("Si vous sortez vainqueur de l'affrontement, rendez-vous au :"))
        st.page_link("tomes/tome7/page_141.py", label="141", icon="📄")
    elif outcome is None:
        st.caption("Vous pouvez fuir le combat après 3 Assauts, par le passage voûté (rendez-vous alors au 241).")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
