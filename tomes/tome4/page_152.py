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

check_inventory(current_page_number=152, book=4)

fr_text = """
En fouillant le cadavre du Garde, vous trouvez les objets suivants :
- 1 Épée,
- 6 Pièces d'Or,
- des vivres équivalant à deux Repas,
- 1 Clé de Cuivre.

Vous pouvez prendre un ou plusieurs de ces objets à condition de
les noter sur votre Feuille d'Aventure. Au moment où vous vous
apprêtez à pénétrer dans le tunnel, un autre Garde apparaît au
pied de la rampe. Il vous voit et donne aussitôt l'alerte en
soufflant dans la corne de guerre qu'il porte autour du cou. Vous
ne perdez pas de temps à attendre de voir ce qui va se passer et
vous vous hâtez de fuir à toutes jambes dans le tunnel, tandis que
les échos de la corne retentissent encore à vos oreilles.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    pickup_button("ÉPÉE", key="epee", label="Prendre l'Épée")
    pickup_gold(6, key="gold")
    pickup_button("REPAS", key="repas_1", label="Prendre 1 Repas")
    pickup_button("REPAS", key="repas_2", label="Prendre 1 Repas")
    pickup_button("CLÉ DE CUIVRE", key="cle_cuivre", label="Prendre la Clé de Cuivre")

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome4/page_81.py", label="81", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
