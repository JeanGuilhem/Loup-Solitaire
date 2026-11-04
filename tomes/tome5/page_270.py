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

check_inventory(current_page_number=270, book=5)

fr_text = """
Vous courez dans la grotte dont le sol est recouvert de cailloux,
impatient de vous éloigner au plus vite du vieillard contaminé.
Les terribles histoires que vous avez entendues au sujet de la
lèpre vous font fuir sans aucune prudence et vous perdez deux
objets de votre Sac à Dos dans votre course folle. Choisissez-en
deux que vous rayerez ensuite de votre Feuille d'Aventure. (Si
vous n'avez pas d'objets dans votre Sac à Dos, vous perdez, à la
place, une Arme et un Objet Spécial.)
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # le choix de la branche est figé dès la première perte (le Sac à Dos peut se vider en cours de route)
    if st.session_state.backpack or st.session_state.get("visibility_perte_sac_1"):
        done = False
        if choose_item_to_lose(
            list(dict.fromkeys(st.session_state.backpack)), key="perte_sac_1",
            label="Choisissez le premier objet perdu :",
        ):
            done = choose_item_to_lose(
                list(dict.fromkeys(st.session_state.backpack)), key="perte_sac_2",
                label="Choisissez le second objet perdu :",
            )
    else:
        done = False
        if choose_item_to_lose(
            list(dict.fromkeys(st.session_state.weapons)), key="perte_arme",
            label="Choisissez l'Arme perdue :",
        ):
            done = choose_item_to_lose(
                list(dict.fromkeys(st.session_state.special)), key="perte_special",
                label="Choisissez l'Objet Spécial perdu :",
            )

    if done:
        st.write_stream(stream_text("Rendez-vous au :"))
        st.page_link("tomes/tome5/page_241.py", label="241", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
