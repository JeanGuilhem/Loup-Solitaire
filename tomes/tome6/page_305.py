import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_magnakai,
    show_illustrations,
    show_map,
)
from text import fr_unknown_magnakai
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=305, book=6)

fr_text = """
Vous traversez le passage voûté et débouchez dans une cour
fermée. Vous apercevez, de l'autre côté, une brèche dans le mur
du château. Vous courez à toute allure en essayant d'éviter les
éboulis de pierres qui encombrent la cour et vous arrivez tout
essoufflé au pied de la brèche. Là, vous remarquez des marches
de pierre qui descendent vers une porte de fer. Vous jetez un
rapide coup d'œil par-dessus votre épaule. Le Yamsark est
toujours lancé à votre poursuite et comble peu à peu son retard,
poussé par la haine et la colère.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez passer à travers la brèche, rendez-vous au :'))
    st.page_link("tomes/tome6/page_217.py", label="217", icon="📄")

    st.write_stream(stream_text('Si vous préférez descendre vers la porte de fer, rendez-vous au :'))
    st.page_link("tomes/tome6/page_169.py", label="169", icon="📄")

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Magnakaï de l'Intuition, rendez-vous au :"))
    if has_magnakai("Intuition"):
        st.page_link("tomes/tome6/page_122.py", label="122", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome6/page_122.py", label="122", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
