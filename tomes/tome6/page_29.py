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

check_inventory(current_page_number=29, book=6)

fr_text = """
Plusieurs flèches se plantent dans votre chair et une douleur
fulgurante vous étreint la poitrine. L'une de vos jambes est
également touchée et vous ne pouvez réprimer un cri. Mais bientôt
la douleur fait place à un terrifiant engourdissement, tandis que
votre cheval continue à vous emporter à vive allure vers les
portes de Tekaro. La dernière chose que vous voyez sont les
chaudrons dangereusement inclinés, déversant par les créneaux des
flots d'huile bouillante et de plomb en fusion. Votre vie et votre
aventure s'achèvent ici.
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
