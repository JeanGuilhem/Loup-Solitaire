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

check_inventory(current_page_number=230, book=4)

fr_text = """
En fouillant les cadavres, vous trouvez les objets suivants :
- 1 Épée,
- 1 Poignard,
- 9 Pièces d'Or,
- des vivres équivalants à 2 Repas.

Vous pouvez prendre un ou plusieurs de ces objets, sans oublier
de les noter sur votre Feuille d'Aventure. Vous entendez alors des
bruits de pas étouffés et vous jetez un coup d'œil inquiet dans le
tunnel. Deux Gardes essaient de s'approcher de vous en se
dissimulant parmi les ombres. Vous parvenez cependant à vous
enfuir avant qu'ils puissent vous attaquer.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    pickup_button("ÉPÉE", key="epee", label="Prendre l'Épée")
    pickup_button("POIGNARD", key="poignard", label="Prendre le Poignard")
    pickup_gold(9, key="gold")
    pickup_button("REPAS", key="repas_1", label="Prendre 1 Repas")
    pickup_button("REPAS", key="repas_2", label="Prendre 1 Repas")

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome4/page_224.py", label="224", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
