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

check_inventory(current_page_number=90, book=6)

fr_text = """
Soudain, un bruit à peine perceptible vous fait faire
volte-face. La vision qui s'offre à vous vous glace d'horreur:
un Dakomyd, un monstre énorme et hideux, bouche entièrement le
tunnel. Il fait plus de trois mètres de haut et ses membres
torses sont chacun prolongés de huit griffes acérées, prêtes à
vous tailler en pièces. Ses gros yeux globuleux apparaissent
entre des paupières jaunes et boursouflées, et sa longue queue
reptilienne fouette rageusement l'air derrière lui. Brusquement,
le monstre passe à l'attaque avant même que vous ne puissiez
réagir, et vous tombez à la renverse dans un trou béant ! Un son
particulièrement odieux emplit la voûte du souterrain et vous
sentez s'abattre sur vous une pluie brûlante et poisseuse.
L'acide transperce vos vêtements puis commence à ronger votre
chair. La dernière chose que vous entendez en ce bas monde est
le ricanement odieux du Dakomyd. Votre aventure et votre vie
s'achèvent ici, dans les égouts de Tekaro.
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
