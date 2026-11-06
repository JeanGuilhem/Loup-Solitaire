import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_magnakai,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=317, book=6)

fr_text = """
Vous vous précipitez hors de la cabane et apercevez votre
compagnon de voyage aux prises avec six cavaliers portant
armure. Cyrilus est maintenant complètement encerclé et toute
résistance est inutile. Il reçoit alors un coup de masse d'armes et
s'effondre inconscient sur l'encolure de son cheval. Quelques
instants après, tous les cavaliers sauf un galopent sur le pont en
emmenant leur captif qu'ils ont ligoté. Le cavalier qui est resté à
l'entrée du pont lève son arbalète et vous vise longuement, alors
que vous courez à toute allure vers votre cheval.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre. Si vous maîtrisez la Discipline Magnakaï de l'Intuition ou de l'Art de la Chasse, ôtez 5 au chiffre obtenu."))
    roll = hazard_roll()
    if roll is not None:
        malus = 5 if has_magnakai("Intuition") or has_magnakai("Art de la Chasse") else 0
        total = roll - malus
        if malus:
            st.write(f"*Malus : -{malus}, soit un total de {total}.*")
        if total <= 6:
            st.write_stream(stream_text('Si votre total est inférieur ou égal à 6, rendez-vous au :'))
            st.page_link("tomes/tome6/page_85.py", label="85", icon="📄")
        else:
            st.write_stream(stream_text('Si votre total est égal ou supérieur à 7, rendez-vous au :'))
            st.page_link("tomes/tome6/page_153.py", label="153", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
