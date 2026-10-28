import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies, ls_death

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=143, book=3)

fr_text = """
Le cône de givre s'enfonce dans le feuillage des plantes en les
gelant instantanément. Tiges et feuilles deviennent alors
cassantes et commencent à céder sous votre poids. Vous essayez
de bondir sur la plateforme où se tient Vonotar, mais il est trop
tard, le pont s'effondre et vous êtes précipité dans le fossé tête la
première. La dernière vision que vous emporterez de ce monde
sera celle d'un Vonotar ricanant qui pointe sur votre tête sa
baguette de cristal. Votre mission s'achève ici en même temps
que votre vie.
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
