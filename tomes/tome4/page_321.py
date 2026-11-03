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

check_inventory(current_page_number=321, book=4)

fr_text = """
La répugnante créature laisse échapper un hurlement de terreur
et meurt devant vous, mais son énorme corps gluant tremble et
se convulse pendant encore plusieurs minutes. Vous attendez un
bon moment avant de vous risquer à vous glisser vers le tunnel
situé derrière le gigantesque cadavre. Il ne reste plus trace de vos
hommes. Leurs corps déjà à demi digérés reposent dans les
entrailles du Ver de Pierre. Saisi de nausée, vous vous hâtez de
fuir ces lieux maléfiques.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome4/page_309.py", label="309", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
