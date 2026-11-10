import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=108, book=7)

fr_text = """
Le courant est tellement fort qu'il vous balaie le long de la ravine
comme un vulgaire fétu et vous emporte au large, en plein milieu
du lac. Le poids de votre équipement, ajouté à la fatigue et aux
eaux gravement polluées ont épuisé presque toutes vos forces.
Vous n'arrivez même plus à maintenir la tête hors de l'eau !
(Vous perdez 5 points d'ENDURANCE à cause du manque d'oxygène.)
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-5)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-5)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome7/page_158.py", label="158", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
