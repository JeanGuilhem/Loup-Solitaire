import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    pickup_button,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=207, book=6)

fr_text = """
En retenant votre respiration, vous passez un nœud coulant au
bout du manche du Marteau de Guerre. Cela vous prend cinq
bonnes minutes pour resserrer le nœud et récupérer l'arme. Il
s'agit d'une très belle arme, faite d'un métal appelé bronin et qui
ressemble en tout point à du bronze fraîchement coulé mais,
contrairement aux alliages ordinaires de cuivre et d'étain, celui-ci
ne se ternit pas et ne s'altère pas avec le temps. Si vous
souhaitez conserver ce Marteau de Guerre de Bronin, inscrivez-le
dans la case Armes de votre Feuille d'Aventure. Lorsque vous
l'utiliserez au cours d'un combat, votre total d'HABILETÉ sera
augmenté de 1 point. Après avoir vérifié qu'aucun autre objet de
valeur n'a été oublié, vous quittez la chapelle et vous partez
rejoindre Cyrilus.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    pickup_button("MARTEAU DE GUERRE DE BRONIN", key="marteau_bronin")

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_338.py", label="338", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
