import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    show_illustrations,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=330, book=2)

fr_text = """
Quelques secondes plus tard, vous vous sentez très mal et vous
sombrez dans l'inconscience. Il s'est écoulé presque une heure lorsque
vous vous réveillez. Vous êtes encore terriblement malade, mais vous
avez survécu aux effets du poison. Vous perdez 5 points
d'ENDURANCE, cependant. Puis, tandis que vos forces reviennent peu
à peu, la fureur vous envahit : vous ramassez vos affaires et vous
quittez aussitôt la chambre d'un pas chancelant, bien décidé à
démasquer celui ou celle qui a tenté de vous assassiner.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-5)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-5)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_200.py", label="200", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
