import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    show_illustrations,
    spend_gold,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=72, book=2)

fr_text = """
L'aubergiste prend votre Pièce d'Or et pose devant vous une chope de
bière mousseuse. C'est une bière forte et revigorante qui vous redonne
un point d'ENDURANCE.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(1)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=1)

    st.write_stream(stream_text("Si vous souhaitez parler à l'aubergiste, rendez-vous au :"))
    st.page_link("tomes/tome2/page_226.py", label="226", icon="📄")

    st.write_stream(
        stream_text(
            "Si vous désirez prendre une chambre pour la nuit, il vous en coûtera 2 Pièces d'Or et vous"
            " vous rendrez au :"
        )
    )
    if st.button("Payer 2 Couronnes (56)", disabled=st.session_state.purse < 2):
        if spend_gold(2):
            st.switch_page("tomes/tome2/page_56.py")
    if st.session_state.purse < 2:
        st.caption("Vous ne possédez pas la somme requise.")

    st.write_stream(
        stream_text(
            "Si enfin vous souhaitez engager une partie de bras de fer, rendez-vous au :"
        )
    )
    st.page_link("tomes/tome2/page_276.py", label="276", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
