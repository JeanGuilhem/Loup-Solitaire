import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=63, book=4)

fr_text = """
Le son d'un glas retentit dans le paysage désolé. Les volets des
fenêtres se ferment en claquant, mais des regards continuent de
vous observer à travers des meurtrières aménagées dans le mur.
Vous faites arrêter vos hommes devant les larges portes de la
taverne. « Nous sommes des soldats du Sommerlund, annoncez-vous,
nous cherchons un abri pour la nuit et du fourrage pour
nos montures. » Après un long moment de silence, une voix vous
répond enfin.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Pour savoir ce qu'elle vous dit, tirez un chiffre à l'aide de la Table de Hasard."))
    number = hazard_roll()
    if number is not None and number <= 4:
        st.write_stream(stream_text("Si ce chiffre est de 0 à 4, rendez-vous au :"))
        st.page_link("tomes/tome4/page_259.py", label="259", icon="📄")
    elif number is not None:
        st.write_stream(stream_text("De 5 à 9, rendez-vous au :"))
        st.page_link("tomes/tome4/page_95.py", label="95", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
