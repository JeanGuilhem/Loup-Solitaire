import streamlit as st
from inventory import (
    check_inventory,
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

check_inventory(current_page_number=118, book=6)

fr_text = """
Vous vous accordez une bonne nuit de repos et vous vous
réveillez peu après le lever du jour, prêt à poursuivre votre
voyage. Mais avant de partir, vous apprenez que la route de
montagne menant à Rhem est impraticable : une avalanche a coupé
la voie sur toute sa largeur, près du Mont Navalyn, et il faudra
sans doute plusieurs semaines pour la déblayer et la remettre en
état. Par conséquent, vous n'avez plus le choix : vous devez
prendre la route de la vallée qui passe par Amory et la forêt
d'Eula. Après avoir rassemblé votre équipement, vous partez sans
perdre de temps. En effet, si vous voulez atteindre Amory avant
la tombée de la nuit, il vous faudra chevaucher à vive allure et
sans prendre le moindre repos.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_96.py", label="96", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
