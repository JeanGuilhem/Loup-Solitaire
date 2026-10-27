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

check_inventory(current_page_number=117, book=2)

fr_text = """
C'est une de ces grosses diligences, semblables à celles qui transportent
les voyageurs de grand chemin au royaume du Sommerlund. Le cocher
tire les rênes et arrête ses chevaux en vous observant de sous le large
bord de son chapeau. Vous lui demandez où il va. « Nous allons à
Ragadorn, répond-il ; nous arriverons là-bas vers midi. Il vous en
coûtera 3 Couronnes pour un billet mais vous pouvez voyager sur le
toit pour une Couronne seulement. »
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez voyager à l'intérieur de la diligence, payez 3 Couronnes au cocher et rendez-vous au :"))
    if st.button("Payer 3 Couronnes (37)", key="pay_37", disabled=st.session_state.purse < 3):
        if spend_gold(3):
            st.switch_page("tomes/tome2/page_37.py")
    if st.session_state.purse < 3:
        st.caption("Vous ne possédez pas la somme requise.")
    st.write_stream(stream_text("Si vous préférez voyager sur le toit, donnez-lui 1 Couronne et rendez-vous au :"))
    if st.button("Payer 1 Couronne (148)", key="pay_148", disabled=st.session_state.purse < 1):
        if spend_gold(1):
            st.switch_page("tomes/tome2/page_148.py")
    if st.session_state.purse < 1:
        st.caption("Vous ne possédez pas la somme requise.")
    st.write_stream(stream_text("Enfin, si vous n'avez pas de quoi payer le voyage, vous n'aurez plus qu'à laisser repartir la diligence et à continuer à pied ; rendez-vous dans ce cas au :"))
    st.page_link("tomes/tome2/page_292.py", label="292", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
