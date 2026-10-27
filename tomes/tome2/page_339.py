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

check_inventory(current_page_number=339, book=2)

fr_text = """
Une demi-heure plus tard, la diligence est arrêtée par des cavaliers en
armes. Ils portent l'emblème de Lachelan, le Suzerain de Ragadorn : un
vaisseau noir surmonté d'une crête rouge. Ils exigent de l'or en
paiement de ce qu'ils appellent une « taxe de sortie » : il en coûtera 1
Couronne à chaque passager. Vos compagnons de voyage déposent
chacun 1 Pièce d'Or sur une assiette qu'ils vous tendent ensuite.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous avez les moyens de payer cette taxe, déposez à votre tour 1 Couronne sur l'assiette ; la diligence alors pourra repartir et vous vous rendrez au :"))
    if st.button("Payer 1 Couronne (249)", key="pay_249", disabled=st.session_state.purse < 1):
        if spend_gold(1):
            st.switch_page("tomes/tome2/page_249.py")
    if st.session_state.purse < 1:
        st.caption("Vous ne possédez pas la somme requise.")
    st.write_stream(stream_text("Si vous n'avez plus d'or, rendez-vous au :"))
    if st.session_state.purse < 1:
        st.page_link("tomes/tome2/page_50.py", label="50", icon="📄")
    else:
        st.caption("Vous avez encore de l'or : vous devez payer.")
        st.page_link("tomes/tome2/page_50.py", label="50", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
