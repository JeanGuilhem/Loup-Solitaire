import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, ls_death

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=161, book=6)

fr_text = """
Alors que vous laissez tomber votre bourse dans la main du
voleur, vous ressentez soudain une douleur suffocante dans les
côtes. « Tu crois qu'on serait assez bête pour te laisser en vie,
maintenant que tu peux nous identifier ? » raille le voleur. Mais
sa voix s'évanouit aussitôt, et vous tombez mollement à terre. Les
deux complices se mêlent rapidement à la foule et, avant que le
meurtre soit découvert, ils auront sans doute déjà gagné l'autre
bout de la ville. Ici se terminent votre vie et votre aventure.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    show_illustrations()
    ls_death()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
