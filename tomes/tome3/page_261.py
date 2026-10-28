import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=261, book=3)

fr_text = """
Lorsque vous arrivez au bas des marches, vous trébuchez et vous
tombez en vous écorchant le genou. Étalé de tout votre long sur
le sol de pierre, vous remarquez alors une ouverture dans le mur
de gauche : il s'agit d'une porte habilement dissimulée parmi les
sculptures contournées qui ornent la paroi. En y regardant de
plus près, vous découvrez un petit levier que vous tirez aussitôt.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome3/page_290.py", label="290", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
