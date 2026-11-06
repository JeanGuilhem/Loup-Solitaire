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

check_inventory(current_page_number=147, book=6)

fr_text = """
L'étroite ruelle est encombrée d'hommes en armes de toutes
sortes : des mercenaires venus du sud à la recherche d'un
engagement. Ils déambulent dans les allées qui s'échappent de la
rue principale, emplissant l'air de leurs cris et de leurs
plaisanteries. Les odeurs de cuisine se mêlent aux relents de
sueur et de cuir, et des petites lanternes à la flamme
crachotante se balancent doucement dans la brise du soir. Au
milieu de cette cohue, personne ne fait attention à vous et vous
avancez sans encombre jusqu'à une magnifique maison à colombage.
Des animaux empaillés et des créatures de toutes espèces,
montées sur des socles de bois, y sont exposés dans de grandes
vitrines. Au-dessus de la porte est inscrit en gros caractères :

**CHANDA TAXIDERMISTE**
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez mettre pied à terre pour entrer dans ce fascinant magasin, rendez-vous au :"))
    st.page_link("tomes/tome6/page_121.py", label="121", icon="📄")

    st.write_stream(stream_text("Si vous préférez continuer à remonter la rue, rendez-vous au :"))
    st.page_link("tomes/tome6/page_279.py", label="279", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
