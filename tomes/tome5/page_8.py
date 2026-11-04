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

check_inventory(current_page_number=8, book=5)

fr_text = """
Vous concentrez toute votre habileté Kaï pour essayer de deviner
le numéro qui déclenche l'ouverture de la porte. C'est une tâche
exténuante, qui requiert toute votre maîtrise mais peu à peu se
forme dans votre esprit l'image de deux chiffres : le 6 et le 7.
Cette image est encore floue et vous ne pouvez pas arriver à
discerner s'il s'agit de 67 ou de 76. Épuisé par l'effort, vous devez
dès à présent déduire 2 points de votre total d'ENDURANCE
avant de prendre une décision.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-2)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-2)

    st.write_stream(stream_text('Si vous optez pour le soixante-sept, rendez-vous au :'))
    st.page_link("tomes/tome5/page_67.py", label="67", icon="📄")
    st.write_stream(stream_text('Si vous préférez choisir le soixante-seize, rendez-vous au :'))
    st.page_link("tomes/tome5/page_76.py", label="76", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
