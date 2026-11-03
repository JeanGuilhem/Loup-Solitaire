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

check_inventory(current_page_number=166, book=4)

fr_text = """
Vous sentez que le chariot abrite plusieurs bandits endormis.
S'ils se réveillent avant que vous n'ayez pu traverser la rivière ou
avant que vous ne vous soyez débarrassé des six brigands en
train de pêcher, vous aurez beaucoup de mal, vos hommes et
vous-même, à leur échapper. Vous estimez donc qu'il est trop
dangereux d'essayer de traverser la rivière à cet endroit et vous
faites signe à vos patrouilleurs de vous suivre en direction de
l'est.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome4/page_232.py", label="232", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
