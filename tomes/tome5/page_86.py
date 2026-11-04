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

check_inventory(current_page_number=86, book=5)

fr_text = """
Vous vous élancez sous le porche tout en surveillant
attentivement les Gardes en train de boire. La poussière soulevée
par les chevaux commence à retomber et, s'ils se retournaient
maintenant, les Gardes vous repéreraient assurément. Dans
votre hâte, vous heurtez du genou une statue en pierre que vous
n'aviez pas remarquée. Réprimant à grand-peine un cri de
douleur, vous boitillez vers les jardins du Palais et vous allez vous
dissimuler derrière l'épais feuillage d'un buisson de Kasl. Votre
blessure vous fait perdre 1 point d'ENDURANCE, mais vous êtes
quand même parvenu à entrer dans le Grand Palais sans être vu !
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-1)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-1)
    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome5/page_137.py", label="137", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
