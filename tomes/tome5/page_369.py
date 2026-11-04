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

check_inventory(current_page_number=369, book=5)

fr_text = """
La terrible douleur contracte tous les muscles de votre corps qui
est secoué par des spasmes incontrôlables. Vous priez pour que
cesse cette agonie et vous perdez 6 points d'ENDURANCE.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-6)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-6)
    st.write_stream(stream_text("Si vous êtes toujours vivant après cette épreuve psychique, rendez-vous au :"))
    st.page_link("tomes/tome5/page_253.py", label="253", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
