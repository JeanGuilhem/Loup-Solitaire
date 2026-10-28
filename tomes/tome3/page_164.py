import streamlit as st
from combat import combat
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=164, book=3)

fr_text = """
Le monstre aux tentacules se hisse hors du fossé et vous attaque.
En même temps, vous remarquez que Vonotar lève sa Crosse
noire en fixant les yeux sur Loi-Kymar. Il est en train d'attaquer
le magicien à l'aide de sa Puissance Psychique. Vous vous rendez
compte alors que si Loi-Kymar est tué, il emportera dans la mort
le secret de la Crosse de la Guilde. Mais avant tout, il vous faut
combattre le monstre. Cette créature est un Akranionor qui
appartient au monde des morts vivants. Vous pourrez donc
multiplier par deux tous les points d'ENDURANCE que votre
adversaire perdra au cours du combat, en raison de la puissance
du Glaive de Sommer.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("AKRANIONOR", 23, 50)], undead=True, max_rounds=5)
    if outcome == "win":
        st.write_stream(stream_text('Vous avez remporté la victoire en 5 Assauts ou moins, rendez-vous au :'))
        st.page_link("tomes/tome3/page_272.py", label="272", icon="📄")
    elif outcome == "rounds_over":
        st.write_stream(stream_text('Le combat se prolonge au-delà de 5 Assauts, rendez-vous au :'))
        st.page_link("tomes/tome3/page_324.py", label="324", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
