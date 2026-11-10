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

check_inventory(current_page_number=101, book=7)

fr_text = """
Subitement, une lourde porte en fer se referme sans crier gare
dans votre dos, condamnant l'accès à la pièce dont vous venez.
Dans le lointain, vous percevez un cliquetis de chaîne et un bruit
de verrous que l'on tire. Votre pouls s'accélère et vous dégainez
instinctivement votre arme, prêt à faire front à une éventuelle
attaque. Plusieurs minutes interminables s'écoulent avant que
vous décidiez de relâcher enfin votre garde.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez aller voir jusqu'où mène ce tunnel, rendez-vous au :"))
    st.page_link("tomes/tome7/page_277.py", label="277", icon="📄")

    st.write_stream(stream_text("Si vous préférez essayer de forcer la porte en fer, rendez-vous au :"))
    st.page_link("tomes/tome7/page_214.py", label="214", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
