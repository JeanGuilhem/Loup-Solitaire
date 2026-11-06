import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, ls_death

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=349, book=6)

fr_text = """
Vous écartez le mince rideau et vous avancez dans la pièce
voûtée. Mais à peine avez-vous posé le pied de l'autre côté, que
vous sentez quelque chose d'anormal. Le sol est mou et
spongieux, et les fines lanières commencent à s'enrouler autour
de vos épaules. Vous venez de pénétrer dans la chambre de
reproduction d'un Dakomyd ! Tandis que l'acide sécrété par les
larves troue vos vêtements et vous brûle la peau, vous entendez
le rire sardonique de la mère Dakomyd retentir dans l'égout.
Votre mission s'achève ici en même temps que votre vie.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    show_illustrations()
    ls_death()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
