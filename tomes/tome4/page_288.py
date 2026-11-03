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

check_inventory(current_page_number=288, book=4)

fr_text = """
Vous postez trois hommes en sentinelle pour garder les chevaux
et vous pénétrez dans la mine en compagnie de quatre
patrouilleurs. Il règne une obscurité totale dans la galerie, mais
vous remarquez bientôt que des Torches éteintes sont accrochées
aux murs humides, à intervalles réguliers, et vous prenez chacun
une torche que vous allumez avant de poursuivre votre chemin.
Les traces de pas sont clairement visibles sur le sol boueux. Elles
mènent à un endroit où le tunnel s'est éboulé. Un amas de terre
se dresse sur le chemin, laissant apparaître une étroite ouverture
entre son sommet et le plafond. Les traces de pas montent le long
de ce tas de terre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez escalader à votre tour le monticule et vous glisser par l'étroite ouverture ménagée entre son sommet et le plafond, rendez-vous au :"))
    st.page_link("tomes/tome4/page_254.py", label="254", icon="📄")
    st.write_stream(stream_text("Si vous préférez interrompre les recherches et retourner à l'entrée du tunnel, rendez-vous au :"))
    st.page_link("tomes/tome4/page_187.py", label="187", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
