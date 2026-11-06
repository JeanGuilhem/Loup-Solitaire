import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
    spend_gold,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=322, book=6)

fr_text = """
Utilisant votre Discipline Magnakaï de l'Invisibilité, vous vous
adressez au sergent en imitant parfaitement le léger nasillement
du dialecte de Quarlen : « Mes plus humbles excuses, sergent,
mais, après avoir passé des années loin de chez moi, je suis
impatient de revoir ma famille. » Le sergent baisse sa lance mais
continue à vous dévisager d'un air soupçonneux. Au bout d'un
moment, certain d'avoir affaire à un authentique citoyen de
Quarlen, il vous adresse un large sourire puis vous dit, en vous
tendant la main : « Nous avons une amende spéciale pour ceux
qui oublient les usages de leur ville natale ; ça fera 10 Pièces d'Or. »
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous acceptez de payer cette somme, rendez-vous au 332.'))
    if st.button("Payer 10 Pièces d'Or", disabled=st.session_state.purse < 10):
        spend_gold(10)
        st.switch_page("tomes/tome6/page_332.py")

    st.write_stream(stream_text("Si vous ne voulez pas vous acquitter de l'amende, prenez la fuite en essayant de sauter par-dessus le chariot et rendez-vous au :"))
    st.page_link("tomes/tome6/page_72.py", label="72", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
