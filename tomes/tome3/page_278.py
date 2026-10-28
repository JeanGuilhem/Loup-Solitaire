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

check_inventory(current_page_number=278, book=3)

fr_text = """
Le premier coup que vous lui portez fracasse le squelette en
projetant ses os alentour. Il ne s'agissait que des restes tout à fait
inoffensifs d'un ancien gardien de tombeau. En examinant l'épée
de plus près, vous vous apercevez que sa couleur noire est
simplement due à la rouille qui recouvre sa lame. Vous abaissez
votre arme et vous montez l'escalier à pas lents.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome3/page_36.py", label="36", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
