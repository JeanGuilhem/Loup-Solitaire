import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import stream_text, called_cookies, hazard_roll

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=210, book=2)

fr_text = """
Vous posez les deux mains sur votre estomac et vous vous concentrez
de toute la force que vous donne la Discipline Kaï pour tenter de
vaincre la douleur. Votre pouvoir de guérison vous soulage bientôt,
mais le poison est puissant et vous n'êtes pas au bout de vos peines.
Utilisez la Table de Hasard pour obtenir un chiffre. Puisse la clémence
des dieux guider votre main, car votre vie dépend désormais du chiffre
que vous aurez tiré !
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    number = hazard_roll()
    if number is not None and number <= 4:
        st.page_link("tomes/tome2/page_275.py", label="275", icon="📄")
    elif number is not None:
        st.page_link("tomes/tome2/page_330.py", label="330", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
