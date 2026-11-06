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

check_inventory(current_page_number=155, book=6)

fr_text = """
Vous tirez une flèche, mais vous manquez de peu votre cible. Le
projectile se fracasse en pure perte contre le mur de la chapelle.
La créature est maintenant sur vous, et vous n'avez
matériellement pas le temps de dégainer une autre arme.
"""

fr_text_2 = """
Vous devrez vous battre à mains nues durant le premier Assaut
de ce combat (déduisez 4 points de votre total d'HABILETÉ pour
ce premier Assaut uniquement). Au début du deuxième Assaut,
vous pouvez tirer votre arme (si toutefois vous en avez une) et
affronter la créature de la façon habituelle.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write(fr_text_2)

    # mains nues au premier assaut (-4, appliqué par le moteur), fuite possible après 4 assauts
    outcome = combat([("YAMSARK", 22, 38)], unarmed_rounds=1, flee_after=4)
    if outcome == "fled":
        st.write_stream(stream_text("Vous échappez au Yamsark en fuyant par le porche de la chapelle ; rendez-vous au :"))
        st.page_link("tomes/tome6/page_305.py", label="305", icon="📄")
    elif outcome == "win":
        st.write_stream(stream_text("Si vous sortez vainqueur de l'affrontement, rendez-vous au :"))
        st.page_link("tomes/tome6/page_112.py", label="112", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
