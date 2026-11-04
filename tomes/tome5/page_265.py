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

check_inventory(current_page_number=265, book=5)

fr_text = """
Elle refuse de prononcer le moindre mot avant que vous n'ayez
déposé un peu d'argent dans sa sébile.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous désirez lui faire l'aumône d'une Pièce d'Or, notez-le sur votre Feuille d'Aventure, et rendez-vous au :"))
    if st.button("Donner 1 Pièce d'Or", disabled=st.session_state.purse < 1):
        spend_gold(1)
        st.switch_page("tomes/tome5/page_397.py")

    st.write_stream(stream_text("Si vous ne souhaitez pas, ou si vous ne pouvez pas lui donner une Pièce d'Or, rendez-vous au :"))
    st.page_link("tomes/tome5/page_256.py", label="256", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
