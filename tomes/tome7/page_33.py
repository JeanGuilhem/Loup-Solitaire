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

check_inventory(current_page_number=33, book=7)

fr_text = """
D'abord, tout n'est que silence. Puis vous percevez un léger
grincement qui va en s'amplifiant au fur et à mesure qu'un
énorme contrepoids entre en action. Le crissement des rouages
vous déchire les oreilles tandis que la herse se lève en s'enfonçant
lentement dans le plafond noir de suie. Sans perdre un instant,
vous vous glissez sous les piques, puis vous vous précipitez dans
le tunnel.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome7/page_277.py", label="277", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
