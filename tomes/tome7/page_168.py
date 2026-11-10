import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    item_info,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=168, book=7)

fr_text = """
L'eau continue à jaillir de la statue, bien que le débit ait
nettement diminué maintenant que la pièce se trouve presque
entièrement remplie. Le visage de l'idole s'est effrité sous la
pression de l'eau, ne laissant qu'un trou large comme une
assiette. En scrutant l'intérieur, vous apercevez un gros ajustage
ainsi qu'un levier, mais tous deux sont profondément enfoncés
dans le corps de la statue, hors de portée de votre bras.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # toute arme de la famille Épée ou Lance (Glaive de Sommer compris)
    carried = st.session_state.weapons + st.session_state.special
    long_weapon = any(item_info(item).get("mastery") in ("ÉPÉE", "LANCE") for item in carried)

    st.write_stream(stream_text("Si vous possédez une Épée ou une Lance, rendez-vous au :"))
    st.page_link("tomes/tome7/page_32.py", label="32", icon="📄", disabled=not long_weapon)

    st.write_stream(stream_text("Si vous n'avez aucune de ces armes, rendez-vous au :"))
    st.page_link("tomes/tome7/page_263.py", label="263", icon="📄", disabled=long_weapon)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
