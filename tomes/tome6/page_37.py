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

check_inventory(current_page_number=37, book=6)

fr_text = """
Soudain, le taxidermiste surgit de derrière un établi sur votre
droite et vous lance une bouteille de verre en plein visage. Vous
esquivez instinctivement le projectile, mais celui-ci vient
heurter votre épaule, vous aspergeant d'un liquide terriblement
corrosif et d'éclats de verre tranchants. Vous perdez 12 points
d'ENDURANCE. Si vous êtes encore en vie à la suite de cette
terrible épreuve, le taxidermiste, loin de s'en tenir à cette
attaque, dégaine une rapière qu'il s'apprête à vous planter en
plein cœur.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-12)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-12)

    outcome = combat([("CHANDA LE TAXIDERMISTE", 17, 24)], flee_after=0)
    if outcome == "fled":
        st.write_stream(stream_text("Si vous souhaitez abandonner le combat à un moment quelconque, sortez vite du magasin, enfourchez votre cheval et rendez-vous au :"))
        st.page_link("tomes/tome6/page_279.py", label="279", icon="📄")
    elif outcome == "win":
        st.write_stream(stream_text("Si vous poursuivez la lutte et que vous en sortez vainqueur, rendez-vous au :"))
        st.page_link("tomes/tome6/page_8.py", label="8", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
