import streamlit as st
from combat import combat
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=114, book=6)

fr_text = """
Vous coupez court aux menaces injurieuses que marmonne le voleur
en lui décochant un coup de poing bien ajusté, tout en le
retenant de l'autre main par le col de sa tunique. L'homme tente
de crier, mais votre coup lui a écrasé le larynx et il n'arrive
à émettre qu'un gargouillement pitoyable. Vous le plaquez dos
contre vous, pour qu'il vous serve de bouclier tandis que son
complice s'élance en brandissant un poignard. L'infortuné reçoit
la terrible lame de plein fouet et il s'écroule sur le sol. Vous
dégainez aussitôt votre arme pour affronter le tueur. La
rapidité de votre attaque vous permet d'ajouter 2 points à votre
total d'HABILETÉ, pour le premier Assaut.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("BRIGAND AU COUTEAU", 15, 22)], first_round_modifier=2)
    if outcome == "win":
        st.write_stream(stream_text("Si vous sortez vainqueur de l'affrontement, rendez-vous au :"))
        st.page_link("tomes/tome6/page_88.py", label="88", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
