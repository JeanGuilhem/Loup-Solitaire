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

check_inventory(current_page_number=103, book=7)

fr_text = """
Vous vous heurtez soudain à une barrière invisible : un champ
magnétique destructeur s'étendant entre les deux piliers verts. Le
choc est rude; vous êtes brutalement rejeté en arrière et vous
tombez à la renverse dans la pièce (vous perdez 8 points
d'ENDURANCE, ou 6 points seulement si vous maîtrisez la
Discipline Magnakaï de Nexus).
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # 8 points perdus, 6 seulement avec Nexus
    loss = 6 if has_magnakai("Nexus") else 8
    if is_new_page():
        change_endurance(-loss)
    if loss:
        st.metric(label="Endurance", value=st.session_state.endurance, delta=-loss)

    st.write_stream(stream_text("Si vous survivez à la collision, rendez-vous au :"))
    st.page_link("tomes/tome7/page_116.py", label="116", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
