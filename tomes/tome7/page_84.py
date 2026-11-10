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

check_inventory(current_page_number=84, book=7)

fr_text = """
Vous ne rencontrez aucune résistance en avançant dans cet
océan de bulles ; vous enfoncez la main dans l'une d'elles comme
s'il s'agissait d'une bulle de savon. Pourtant, lorsque vous tentez
de la retirer, la membrane transparente se referme, tel un étau,
sur votre poignet. Vous voici prisonnier, et le loup se rapproche !
Il bondit sur vous et vous plante ses crocs dans la jambe, tandis
que vous sentez la partie supérieure de votre corps se faire
rapidement absorber par la monstrueuse bulle. En l'espace de
quelques secondes, vous êtes simultanément mis en pièces par le
loup et asphyxié par la bulle. Cela marque la fin de votre triste
aventure.
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
