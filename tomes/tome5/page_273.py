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

check_inventory(current_page_number=273, book=5)

fr_text = """
L'Akataz vous saute au visage et, sous la violence du choc, vous
tombez à la renverse. Vous essayez de vous relever, mais le chien
vous mord à l'épaule et vous avez le souffle coupé pendant
quelques instants. (Vous perdez 1 point d'ENDURANCE.)
Finalement, vous parvenez, par un puissant coup de pied, à
l'envoyer rouler au bas des marches. Il s'écrase en hurlant sur le
sol de marbre du Palais inférieur. Vous sautez sur vos pieds et
vous tirez votre arme car les Drakkars courent à présent vers
vous. Un terrible hurlement de haine et de rage emplit le hall :
« Tuez-le ! » Les Drakkars dégainent leurs épées noires, impatients
d'obéir à l'ordre de leur maître. Ils vous attaquent tous ensemble.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-1)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-1)

    st.write_stream(stream_text("Vous pouvez interrompre le combat à tout moment en courant vers le passage voisin."))
    outcome = combat([("DRAKKARS", 18, 35)], flee_after=0)
    if outcome == "fled":
        st.write_stream(stream_text("Si vous souhaitez fuir la bataille, rendez-vous au :"))
        st.page_link("tomes/tome5/page_238.py", label="238", icon="📄")
    elif outcome == "win":
        st.write_stream(stream_text("Si vous remportez le combat, rendez-vous au :"))
        st.page_link("tomes/tome5/page_345.py", label="345", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
