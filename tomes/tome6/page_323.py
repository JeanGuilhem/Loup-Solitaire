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

check_inventory(current_page_number=323, book=6)

fr_text = """
Vous enfoncez votre arme très profondément dans la chair
visqueuse du Dakomyd. La puanteur abominable qui se dégage
de sa blessure est telle que vous devez vous boucher le nez. Une
giclée de sang aqueux vous atteint au bras et coule sur votre
arme. Le sang transperce votre tunique et vous brûle la peau, et
votre arme se désintègre, corrodée par le sang. Avant que vous
puissiez vous enfuir, des griffes acérées vous tirent par le
manteau et vous entraînent vers la mort. Votre vie et votre quête
s'achèvent ici, dans la crypte de la Cathédrale de Tekaro.
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
