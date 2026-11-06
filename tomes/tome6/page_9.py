import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
    spend_gold,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=9, book=6)

fr_text = """
Les gardes échangent un regard entendu puis ils acquiescent de la
tête. « 10 Pièces d'Or et vous serez le bienvenu dans notre ville,
noble étranger », dit le plus petit des deux hommes en tendant sa
main gantée pour recevoir son dû.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous acceptez de payer, rendez-vous au 332."))
    if st.button("Payer 10 Couronnes", disabled=st.session_state.purse < 10):
        spend_gold(10)
        st.switch_page("tomes/tome6/page_332.py")

    st.write_stream(stream_text("Si vous estimez que la somme demandée est exorbitante, vous pouvez tenter de contourner les gardes et de forcer le passage, rendez-vous au :"))
    st.page_link("tomes/tome6/page_261.py", label="261", icon="📄")

    st.write_stream(stream_text("Si vous préférez décliner poliment la proposition et essayer d'entrer dans la ville par la porte nord, rendez-vous au :"))
    st.page_link("tomes/tome6/page_137.py", label="137", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
