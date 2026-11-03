import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=263, book=4)

fr_text = """
Vous vous penchez de côté pour essayer d'esquiver le projectile,
mais le disque s'enfonce profondément dans votre épaule et vous
perdez 4 points d'ENDURANCE. La main crispée sur votre bras
blessé, vous courez le long d'un chemin étroit qui mène à un
bosquet d'arbres au feuillage touffu. Lorsque vous l'atteignez,
vous entendez derrière vous les cris des brigands.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-4)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-4)
    st.write_stream(stream_text('Si vous souhaitez poursuivre votre fuite à travers la forêt en direction du sud, rendez-vous au :'))
    st.page_link("tomes/tome4/page_123.py", label="123", icon="📄")
    st.write_stream(stream_text("Si vous préférez changer de direction et courir vers l'ouest, rendez-vous au :"))
    st.page_link("tomes/tome4/page_169.py", label="169", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
