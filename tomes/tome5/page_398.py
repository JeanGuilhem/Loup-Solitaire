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

check_inventory(current_page_number=398, book=5)

fr_text = """
Le Garde lève le bras puis ôte la fléchette de sa nuque. Mais avant
qu'il n'ait le temps de comprendre ce qui lui arrive, il s'effondre
au sol, inconscient, étalé de tout son long sur la plate-forme
d'atterrissage. Vous entendez des bruits de pas qui retentissent
par-delà les toits du Palais : les Drakkars sont à vos trousses.
Vous devez agir rapidement si vous voulez leur échapper.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez fouiller le corps du Garde endormi, rendez-vous au :"))
    st.page_link("tomes/tome5/page_207.py", label="207", icon="📄")
    st.write_stream(stream_text("Si vous préférez ne pas vous occuper du Garde et vous précipiter directement vers l'enclos de l'Itikar, rendez-vous au :"))
    st.page_link("tomes/tome5/page_224.py", label="224", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
