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

check_inventory(current_page_number=131, book=5)

fr_text = """
Vous examinez les nombreux objets disposés sur la grande table,
faisant le tri entre ceux qui pourraient vous être utiles et les
autres. Voici la liste des objets :
- un Peigne d'Argent,
- 1 Sablier,
- 1 Poignard,
- 1 Potion de Laumspur (qui vous redonnera 4 points
d'ENDURANCE si vous en avalez une dose après un combat),
- 1 Prisme
- et suffisamment de provisions pour 3 Repas (chaque
Repas équivaut à un objet que vous inscrirez dans la case Sac à
Dos de votre Feuille d'Aventure).

Faites les modifications nécessaires sur votre Feuille d'Aventure
avant de quitter la pièce.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    pickup_button("PEIGNE D'ARGENT", key="peigne", label="Prendre le Peigne d'Argent")
    pickup_button("SABLIER", key="sablier", label="Prendre le Sablier")
    pickup_button("POIGNARD", key="poignard", label="Prendre le Poignard")
    pickup_button("POTION DE LAUMSPUR", key="laumspur", label="Prendre la Potion de Laumspur")
    pickup_button("PRISME", key="prisme", label="Prendre le Prisme")
    pickup_button("REPAS", key="repas_1", label="Prendre 1 Repas")
    pickup_button("REPAS", key="repas_2", label="Prendre 1 Repas")
    pickup_button("REPAS", key="repas_3", label="Prendre 1 Repas")

    st.write_stream(stream_text("Rendez-vous ensuite au :"))
    st.page_link("tomes/tome5/page_58.py", label="58", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
