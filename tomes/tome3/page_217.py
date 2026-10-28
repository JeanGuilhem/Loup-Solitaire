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
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=217, book=3)

fr_text = """
Le monolithe explose soudain, projetant en tous sens des
centaines d'éclats tranchants comme des rasoirs. Vous êtes criblé
par les fragments de pierre et la seule force de l'explosion vous
précipite sur le sol. Vous perdez 10 points d'ENDURANCE.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-10)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-10)
    st.write_stream(stream_text("Si vous êtes toujours vivant, rendez-vous au :"))
    st.page_link("tomes/tome3/page_154.py", label="154", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
