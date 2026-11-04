import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    choose_item_to_lose,
    display_inventory,
    end_page,
    is_new_page,
    lose_gold,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=40, book=5)

fr_text = """
En tombant à l'eau, le Kwaraz que vous venez de tuer crée un
énorme remous et vous êtes soudain submergé par une vague de
liquide putride. Saisi de nausée, vous vous mettez à tousser pour
essayer de maîtriser de pénibles haut-le-cœur, tout en chassant
les saletés de vos yeux et de votre bouche. Le cadavre du Kwaraz
obstrue le tunnel et le seul moyen de passer est de l'enjamber.
Encore sous le choc de vos émotions, vous perdez à cette
occasion un objet de votre Sac à Dos, vos Pièces d'Or et 2 points
d'ENDURANCE. N'oubliez pas de noter toutes ces modifications
sur votre Feuille d'Aventure.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        lose_gold()
        change_endurance(-2)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-2)
    st.warning("Vous avez perdu vos Pièces d'Or.")
    if choose_item_to_lose(list(st.session_state.backpack), key="kwaraz", label="Choisissez l'objet du Sac à Dos que vous perdez :"):
        st.write_stream(stream_text('Si vous êtes encore en vie, rendez-vous à présent au :'))
        st.page_link("tomes/tome5/page_17.py", label="17", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
