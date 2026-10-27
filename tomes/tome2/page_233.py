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

check_inventory(current_page_number=233, book=2)

fr_text = """
« Nous allons à Ragadorn, nous devrions arriver là-bas vers midi, dit-il,
le visage presque entièrement dissimulé sous son chapeau à larges
bords, le billet coûte 3 Couronnes, mais si vous voulez voyager sur le
toit, vous n'aurez qu'une seule couronne à payer. »
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez faire le voyage à l'intérieur de la diligence, donnez 3 Couronnes au cocher et rendez-vous au :"))
    if st.button("Payer 3 Couronnes (37)", key="pay_37", disabled=st.session_state.purse < 3):
        if spend_gold(3):
            st.switch_page("tomes/tome2/page_37.py")
    if st.session_state.purse < 3:
        st.caption("Vous ne possédez pas la somme requise.")

    st.write_stream(stream_text('Si vous préférez faire le trajet sur le toit, donnez-lui 1 Couronne et rendez-vous au :'))
    if st.button("Payer 1 Couronne (148)", key="pay_148", disabled=st.session_state.purse < 1):
        if spend_gold(1):
            st.switch_page("tomes/tome2/page_148.py")
    if st.session_state.purse < 1:
        st.caption("Vous ne possédez pas la somme requise.")

    st.write_stream(stream_text("Si vous n'avez pas les moyens de payer, il ne vous reste plus qu'à repartir à pied en vous rendant au :"))
    st.page_link("tomes/tome2/page_292.py", label="292", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
