import streamlit as st
from inventory import (
    add_to_inventory,
    can_shoot,
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

check_inventory(current_page_number=31, book=7)

fr_text = """
Vous ne laissez aucune chance à vos ennemis : vous les éliminez
tous les trois en autant de coups, puis vous recouvrez leurs corps
avec une tapisserie que vous arrachez du mur. Il n'y avait rien
d'intéressant dans les poches de vos victimes mais, en revanche,
vous découvrez sur la table un Passe-Partout et un Parchemin.
Ces deux objets pourraient peut-être vous servir à un moment
donné, aussi décidez-vous de les garder. (Inscrivez-les dans la
case Objets Spéciaux de votre Feuille d'Aventure, puis glissez-les
dans une de vos poches.) Cela fait, vous quittez la pièce. Mais à
peine avez-vous fait un pas dans le couloir que vous vous trouvez
nez à nez avec un garde en armure. En poussant un cri étouffé
par la visière de son heaume, il fait demi-tour et part en courant
vers une corde qui descend du plafond.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        add_to_inventory("PASSE-PARTOUT")
        add_to_inventory("PARCHEMIN")
        st.success("Le Passe-Partout et le Parchemin sont inscrits dans vos Objets Spéciaux.")

    st.write_stream(stream_text('Si vous avez un arc et si vous désirez vous en servir, rendez-vous au :'))
    st.page_link("tomes/tome7/page_266.py", label="266", icon="📄", disabled=not can_shoot())

    st.write_stream(stream_text("Si vous n'avez pas d'arc, ou si vous ne voulez pas l'utiliser, rendez-vous au :"))
    st.page_link("tomes/tome7/page_40.py", label="40", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
