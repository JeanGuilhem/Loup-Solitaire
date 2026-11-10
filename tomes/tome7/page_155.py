import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=155, book=7)

fr_text = """
Vous êtes soudain aveuglé par un vif éclair blanc ; aussitôt après,
des jets de flammes jaillissent des murs et du plafond. Ils sont si
nombreux, et la lumière qu'ils dégagent est si intense, que vous
ne pouvez même pas voir où ils se terminent. Une vague de
chaleur suffocante vous fouette le visage, et vous vous voyez
contraint de reculer vers le loup affamé.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez affronter sur place le féroce animal, rendez-vous au :"))
    st.page_link("tomes/tome7/page_120.py", label="120", icon="📄")

    st.write_stream(stream_text("Si vous préférez vous précipiter dans le brasier infernal afin d'échapper au loup, rendez-vous au :"))
    st.page_link("tomes/tome7/page_204.py", label="204", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
