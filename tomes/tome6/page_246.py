import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    pickup_button,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=246, book=6)

fr_text = """
Le monstre passe à quelques centimètres de votre cachette mais,
par miracle, il ne vous voit pas. Son rire affreux se perd peu à peu
dans l'obscurité. Vous sortez de la niche et vous grimpez les
marches quatre à quatre. Dans la chapelle, vous retrouvez votre
flacon de verre intact et vous le remplissez aussitôt d'Eau de
Taunor. (L'eau thermale peut vous faire regagner 6 points
d'ENDURANCE.) Vous pouvez boire l'eau dès maintenant ou
mettre le Flacon dans votre Sac à Dos pour plus tard. (N'oubliez
pas d'inscrire votre Flacon sur votre Feuille d'Aventure, comme
Objet de Sac à Dos.) Vous décidez ensuite de rejoindre Cyrilus
sans plus attendre car le Yamsark est toujours en liberté et peut
attaquer de nouveau à tout moment.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    taken = st.session_state.get("visibility_taunor", False)
    if st.button("Boire l'Eau de Taunor maintenant (+6 ENDURANCE)", disabled=taken):
        if not st.session_state.get("visibility_taunor", False):
            change_endurance(6)
            st.session_state["visibility_taunor"] = True
            st.rerun()
    pickup_button("EAU DE TAUNOR", key="taunor", label="Garder le Flacon d'Eau de Taunor dans le Sac à Dos")

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_338.py", label="338", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
