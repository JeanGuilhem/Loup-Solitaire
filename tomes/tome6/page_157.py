import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    pickup_button,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=157, book=6)

fr_text = """
Le pain que vous mangez est encore meilleur que l'odeur le
laissait présager (vous gagnez 1 point d'ENDURANCE). Si vous le
désirez, vous pouvez en emporter l'équivalent de 2 Repas. Dans
ce cas, n'oubliez pas de l'inscrire sur votre Feuille d'Aventure. Au
moment où vous vous apprêtez à contourner le comptoir pour
aller inspecter l'arrière-salle, vous entendez soudain un cri de
détresse au-dehors. C'est la voix de Cyrilus, il doit être en
difficulté !
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(1)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=1)

    pickup_button("REPAS", key="pain_1", label="Emporter 1 Repas de pain")
    pickup_button("REPAS", key="pain_2", label="Emporter 1 autre Repas de pain")

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_317.py", label="317", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
