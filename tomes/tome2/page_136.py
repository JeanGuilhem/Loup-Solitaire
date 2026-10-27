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

check_inventory(current_page_number=136, book=2)

fr_text = """
« Il vous en coûtera 20 Couronnes pour vous rendre à Port Bax », lance
le cocher qui s'exprime avec un fort accent de Ragadorn.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous possédez ces 20 Couronnes et que vous souhaitez acheter un billet, rendez-vous au :"))
    if st.button("Payer 20 Couronnes (10)", key="pay_10", disabled=st.session_state.purse < 20):
        if spend_gold(20):
            st.switch_page("tomes/tome2/page_10.py")
    if st.session_state.purse < 20:
        st.caption("Vous ne possédez pas la somme requise.")
    st.write_stream(stream_text("Si vous n'avez pas assez d'argent, rendez-vous au :"))
    st.page_link("tomes/tome2/page_238.py", label="238", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
