import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=60, book=7)

fr_text = """
Dès que votre main effleure la brume, un fulgurant éclair bleu
jaillit d'un coin du plafond. Une douleur insoutenable vous
traverse le bras et vous êtes catapulté dans l'eau sous la force du
choc. (Vous perdez 4 points d'ENDURANCE.)
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-4)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-4)

    pills = has_item("FIOLE DE PILULES BLEUES")
    st.write_stream(stream_text("Si vous possédez un flacon de Pilules Bleues, rendez-vous au :"))
    st.page_link("tomes/tome7/page_230.py", label="230", icon="📄", disabled=not pills)
    st.write_stream(stream_text("Si vous ne possédez pas cet Objet, rendez-vous au :"))
    st.page_link("tomes/tome7/page_263.py", label="263", icon="📄", disabled=pills)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
