import streamlit as st
from inventory import (
    check_inventory,
    choose_item_to_lose,
    count_item,
    display_inventory,
    end_page,
    is_new_page,
    remove_from_inventory,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=158, book=7)

fr_text = """
Suffoqué par le manque d'oxygène, vous remontez péniblement à
la surface et nagez vers le rivage. Vous vous hissez ensuite hors
de l'eau et vous affalez, plus mort que vif, près d'un groupe de
rochers à moitié enterrés dans le sable noir de la plage. Au cours
de cette baignade forcée, vous avez perdu deux Objets de votre
Sac à Dos, et l'eau polluée a abîmé toutes vos Provisions (rayez
tous les Repas de votre Feuille d'Aventure, ainsi que deux Objets
de Sac à Dos). A peine avez-vous eu le temps de reprendre votre
souffle qu'un grattement sonore se fait entendre, comme si on
traînait quelque chose de très lourd entre les rochers. Soudain,
une fissure verticale apparaît à la surface du rocher qui se trouve
juste à votre gauche ; il en jaillit un faisceau de lumière jaune qui
se pose sur vous. Ce n'est pas un rocher, mais un œil énorme !
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        meals = count_item("REPAS")
        if meals:
            remove_from_inventory("REPAS", meals)
    st.caption("Tous vos Repas sont rayés de votre Feuille d'Aventure.")

    # deux Objets de Sac à Dos perdus, au choix du joueur (les Repas sont déjà rayés)
    first_lost = choose_item_to_lose(
        list(dict.fromkeys(st.session_state.backpack)),
        key="lost_158_first",
        label="Choisissez le premier Objet de Sac à Dos perdu :",
    )
    second_lost = first_lost and choose_item_to_lose(
        list(dict.fromkeys(st.session_state.backpack)),
        key="lost_158_second",
        label="Choisissez le second Objet de Sac à Dos perdu :",
    )
    pending = not second_lost
    if pending:
        st.warning("Choisissez d'abord les deux Objets de Sac à Dos que vous avez perdus.")

    st.write_stream(stream_text("Si vous voulez dégainer votre arme et attaquer la monstrueuse pupille, rendez-vous au :"))
    st.page_link("tomes/tome7/page_265.py", label="265", icon="📄", disabled=pending)

    st.write_stream(stream_text("Si vous préférez vous remettre debout et fuir vers l'à-pic rocheux qui soutient Kazan-Oud, rendez-vous au :"))
    st.page_link("tomes/tome7/page_41.py", label="41", icon="📄", disabled=pending)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
