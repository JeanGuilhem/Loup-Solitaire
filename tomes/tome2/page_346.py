import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    spend_gold,
)
from utils import called_cookies, handle_repas, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=346, book=2)

fr_text = """
Le cocher hoche la tête et vous rend le billet. L'auberge est bien
chauffée, mais pauvrement meublée. Vous allez devoir prendre ici un
repas qui vous coûtera 1 Couronne, à moins que vous n'ayez de quoi
manger dans votre Sac à Dos. Si vous ne possédez ni or ni nourriture,
vous perdez 3 points d'ENDURANCE. Si vous maîtrisez la Discipline
Kaï de la Chasse, vous ne pourrez pas vous en servir tant que vous
traverserez le Pays Sauvage, car c'est un désert entièrement aride où ne
vivent que des Squalls, des créatures chétives et couardes apparentées
aux Gloks et tout à fait impropres à la consommation.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    handle_repas(gold_cost=1, hunting=False)

    st.write_stream(stream_text("Si vous avez les moyens de vous offrir une chambre au prix de 1 Couronne, rendez-vous au :"))
    if st.button("Payer 1 Couronne pour une chambre (280)", key="pay_280", disabled=st.session_state.purse < 1):
        if spend_gold(1):
            st.switch_page("tomes/tome2/page_280.py")
    if st.session_state.purse < 1:
        st.caption("Vous ne possédez pas la somme requise.")
    st.write_stream(stream_text("Si vous n'avez pas d'argent, rendez-vous au :"))
    if st.session_state.purse < 1:
        st.page_link("tomes/tome2/page_205.py", label="205", icon="📄")
    else:
        st.caption("Vous avez encore de l'or : vous devez payer.")
        st.page_link("tomes/tome2/page_205.py", label="205", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
