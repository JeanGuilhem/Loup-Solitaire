import streamlit as st
from inventory import (
    check_inventory,
    choose_item_to_lose,
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

check_inventory(current_page_number=131, book=7)

fr_text = """
Après vous être libéré des derniers fils poisseux, vous grimpez
l'escalier en courant, puis vous franchissez le portail grand
ouvert. Vous réalisez alors que, lors de votre combat contre la
Toile-Piège, vous avez perdu une Arme et un Objet de votre Sac à
Dos. (Rayez, au choix, une Arme et un Objet de votre Feuille
d'Aventure.) Vous vous trouvez à présent dans une espèce
d'entrepôt en ruine. A travers la vitre brisée de la seule fenêtre en
ogive qui éclaire la pièce, vous apercevez les contours lugubres
d'un grand édifice à moitié effondré, flanqué d'un donjon noirci
par le feu ; ce sont les ruines de Kazan-Oud.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # rayez au choix une Arme et un Objet du Sac à Dos
    weapon_done = choose_item_to_lose(list(dict.fromkeys(st.session_state.weapons)), key="t7_131_weapon",
                                      label="Choisissez l'Arme perdue :")
    item_done = weapon_done and choose_item_to_lose(list(dict.fromkeys(st.session_state.backpack)),
                                                    key="t7_131_item", label="Choisissez l'Objet du Sac à Dos perdu :")
    if item_done:
        st.write_stream(stream_text("Rendez-vous au :"))
        st.page_link("tomes/tome7/page_27.py", label="27", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
