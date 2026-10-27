import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    spend_gold,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=217, book=2)

fr_text = """
L'homme vous regarde et vous répond d'une voix bourrue: «La
diligente... il faut prendre la diligence qui part cet après-midi pour Port
Bax. Si vous me donnez 1 Couronne, je vous dirai comment vous
rendre au relais. »
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous acceptez de payer, déduisez la Couronne de votre capital et rendez-vous au :'))
    if st.button("Payer 1 Couronne (199)", key="pay_199", disabled=st.session_state.purse < 1):
        if spend_gold(1):
            st.switch_page("tomes/tome2/page_199.py")
    if st.session_state.purse < 1:
        st.caption("Vous ne possédez pas la somme requise.")

    st.write_stream(stream_text("Si vous préférez quitter l'auberge sans lui donner la Pièce d'Or qu'il demande, rendez-vous au :"))
    st.page_link("tomes/tome2/page_143.py", label="143", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
