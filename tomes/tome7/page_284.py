import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    has_magnakai,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=284, book=7)

fr_text = """
Vous vous couvrez le nez avec votre manteau Kaï et vous avancez
vers le tunnel en contournant les flammes. Vous allez franchir
l'entrée, lorsque vous vous heurtez à une barrière invisible : un
champ d'énergie destructrice qui s'étend entre les deux piliers
verts. Vous êtes aussitôt violemment rejeté en arrière par une
énorme secousse. (Vous perdez 8 points d'ENDURANCE. Si vous
maîtrisez la Discipline Magnakaï de Nexus, vous ne perdez que 6
points d'ENDURANCE.)
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    loss = 6 if has_magnakai("Nexus") else 8
    if is_new_page():
        change_endurance(-loss)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-loss)

    st.write_stream(stream_text("Si vous êtes toujours en vie, rendez-vous au :"))
    st.page_link("tomes/tome7/page_128.py", label="128", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
