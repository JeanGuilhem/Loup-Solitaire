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

check_inventory(current_page_number=102, book=5)

fr_text = """
Après une fouille minutieuse des corps, vous trouvez les objets
suivants :
- 1 Epée,
- 1 Poignard,
- 1 Marteau de Guerre,
- 6 Pièces d'Or
- et les Clés du Geôlier (Objet Spécial).

Vous pouvez prendre les objets que vous voulez, mais n'oubliez
pas de les noter sur votre Feuille d'Aventure. Si vous prenez les
Clés du Geôlier, portez-les accrochées à votre ceinture. Après
avoir verrouillé la porte de la cellule, vous vous hâtez le long du
couloir.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    pickup_button("ÉPÉE", key="epee", label="Prendre l'Épée")
    pickup_button("POIGNARD", key="poignard", label="Prendre le Poignard")
    pickup_button("MARTEAU DE GUERRE", key="marteau", label="Prendre le Marteau de Guerre")
    pickup_gold(6, key="gold")
    pickup_button("CLÉS DU GEÔLIER", key="cles", label="Prendre les Clés du Geôlier")

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome5/page_150.py", label="150", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
