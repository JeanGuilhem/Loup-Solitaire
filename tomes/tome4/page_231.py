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

check_inventory(current_page_number=231, book=4)

fr_text = """
Votre attaque est fulgurante et mortelle. Le Garde meurt avant
même de s'être effondré sur le sol. En fouillant son cadavre vous
trouvez les objets suivants :
- 3 Pièces d'Or,
- 1 Épée,
- des provisions équivalantes à 1 Repas.

Vous pouvez prendre un ou plusieurs de ces objets avant de
traverser le pont. N'oubliez pas de les noter sur votre Feuille
d'Aventure. Lorsque vous arrivez de l'autre côté du pont, vous
entendez des bruits de pas lointains et précipités. Il vous semble
préférable de ne pas vous attarder plus longtemps et vous
pénétrez aussitôt dans le tunnel orienté à l'ouest.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    pickup_gold(3, key="gold")
    pickup_button("ÉPÉE", key="epee", label="Prendre l'Épée")
    pickup_button("REPAS", key="repas_1", label="Prendre 1 Repas")

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome4/page_348.py", label="348", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
