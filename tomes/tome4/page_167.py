import streamlit as st
from inventory import (
    add_to_inventory,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    pickup_button,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=167, book=4)

fr_text = """
Vous avez la satisfaction de découvrir au fond du chariot de mine
un Sac à Dos de mineur et une Pelle. A l'intérieur du Sac à Dos,
vous trouvez des provisions équivalant à un Repas. Vous ajustez
le Sac à Dos sur vos épaules puis vous montez la pente raide du
tunnel. Apportez à votre Feuille d'Aventure les modifications
nécessaires.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page() and not st.session_state.has_backpack:
        add_to_inventory("SAC À DOS")
    pickup_button("PELLE", key="pelle", label="Prendre la Pelle")
    pickup_button("REPAS", key="repas_1", label="Prendre 1 Repas")

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome4/page_185.py", label="185", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
