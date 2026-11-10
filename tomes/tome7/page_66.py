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

check_inventory(current_page_number=66, book=7)

fr_text = """
Vous examinez attentivement la gâche qui bloque le mécanisme
de fermeture : si vous arriviez seulement à la repousser, vous
pourriez alors tirer le verrou.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # toute épée convient (Épée, Glaive de Sommer, autre arme de la famille des épées)
    sword = any(
        item_info(item).get("mastery") == "ÉPÉE"
        for item in st.session_state.weapons + st.session_state.special
    )
    st.write_stream(stream_text("Si vous possédez une épée, rendez-vous au :"))
    st.page_link("tomes/tome7/page_252.py", label="252", icon="📄", disabled=not sword)
    st.write_stream(stream_text("Sinon, inutile de vous acharner sur cette porte. Seule la statue peut maintenant vous offrir une chance de sortie ; rendez-vous au :"))
    st.page_link("tomes/tome7/page_168.py", label="168", icon="📄", disabled=sword)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
