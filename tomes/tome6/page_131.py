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

check_inventory(current_page_number=131, book=6)

fr_text = """
Grâce à votre vue perçante, vous repérez soudain une ligne
sombre en aval. Il s'agit d'une rangée de rondins attachés les
uns aux autres par de grosses chaînes en métal : un barrage
flottant, tendu en plein travers de la rivière ! Vous prenez
immédiatement conscience du péril, et vous vous ruez sur le pont
pour avertir le timonier : « Attention ! Il y a un barrage droit
devant ! » L'homme tourne aussitôt la barre en grande hâte, mais
il est trop tard pour éviter la collision. Un bruit de métal
tordu et de bois éclaté déchire le silence au moment où le
Kazonara heurte par le travers les gros troncs d'arbres
enchaînés. Vous vous arc-boutez et vous vous agrippez fermement
au bastingage tandis que l'embarcation tangue et fait de
brusques embardées.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_224.py", label="224", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
