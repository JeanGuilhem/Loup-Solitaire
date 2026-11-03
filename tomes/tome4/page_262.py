import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, ls_death

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=262, book=4)

fr_text = """
Vous vous ruez en avant pour frapper, mais le brigand cabre son
cheval et esquive votre coup. Les sabots de l'étalon s'abattent sur
votre tête, vous tombez à terre et vous êtes piétiné dans une mare
de sang. Assommé et mortellement blessé, vous percevez à peine
le ricanement maléfique du cavalier qui lève son arme pour vous
porter le coup de grâce. Votre mission s'achève ici en même
temps que votre vie.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    show_illustrations()
    ls_death()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
