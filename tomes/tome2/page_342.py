import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    spend_gold,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=342, book=2)

fr_text = """
C'est une véritable montagne humaine, le crâne complètement chauve
et les oreilles ornées de gros anneaux d'or. Il vous regarde d'un air
soupçonneux avant de vous adresser enfin la parole : « Une bière coûte
1 Pièce d'Or, une chambre 2 Pièces. Qu'est-ce que vous choisissez ? »
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez prendre une bière, payez une Pièce d'Or et rendez-vous au :"))
    if st.button("Payer 1 Couronne pour une bière (72)", key="pay_72", disabled=st.session_state.purse < 1):
        if spend_gold(1):
            st.switch_page("tomes/tome2/page_72.py")
    if st.session_state.purse < 1:
        st.caption("Vous ne possédez pas la somme requise.")
    st.write_stream(stream_text("Si vous préférez louer une chambre pour la nuit, payez 2 Pièces d'Or à l'aubergiste et rendez-vous au :"))
    if st.button("Payer 2 Couronnes pour une chambre (56)", key="pay_56", disabled=st.session_state.purse < 2):
        if spend_gold(2):
            st.switch_page("tomes/tome2/page_56.py")
    if st.session_state.purse < 2:
        st.caption("Vous ne possédez pas la somme requise.")
    st.write_stream(stream_text("Si vous n'avez besoin ni de l'une ni de l'autre, vous pouvez demander plutôt à cet homme de vous parler de Ragadorn ; rendez-vous pour cela au :"))
    st.page_link("tomes/tome2/page_226.py", label="226", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
