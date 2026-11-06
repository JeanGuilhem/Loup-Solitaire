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

check_inventory(current_page_number=51, book=6)

fr_text = """
Vous ne pouvez réprimer un hoquet de douleur lorsque la lame
vous entaille la hanche, avant d'aller se planter profondément
dans le bois du bastingage. (Vous perdez 2 points d'ENDURANCE.)
Le pirate, rendu fou furieux de vous voir encore en vie, se
précipite sur vous, mais vous parvenez à esquiver son attaque.
Perdant l'équilibre, votre adversaire bascule par-dessus le
parapet et tombe dans les eaux glaciales et profondes de la
Storn.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-2)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-2)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_254.py", label="254", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
