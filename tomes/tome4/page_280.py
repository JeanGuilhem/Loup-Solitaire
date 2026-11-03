import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    pickup_button,
    pickup_gold,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=280, book=4)

fr_text = """
Vous retournez le cadavre et vous le fouillez rapidement. Vous
découvrez alors les objets suivants :
- 3 Pièces d'Or,
- des provisions équivalant à 1 Repas.
- 1 Epée.
Vous pouvez prendre un ou plusieurs de ces objets avant de
franchir le pont. N'oubliez pas de les noter sur votre Feuille
d'Aventure. Lorsque vous parvenez de l'autre côté de la
passerelle, vous entendez des bruits de pas lointains et
précipités. Vous estimez préférable de ne pas vous attarder plus
longtemps et vous quittez les lieux en empruntant le tunnel qui
s'ouvre dans le mur ouest.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    pickup_gold(3, key="gold")
    pickup_button("REPAS", key="repas_1", label="Prendre 1 Repas")
    pickup_button("ÉPÉE", key="epee", label="Prendre l'Épée")
    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome4/page_348.py", label="348", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
