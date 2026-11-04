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

check_inventory(current_page_number=155, book=5)

fr_text = """
La vue qui s'offre à vous vous indique que la fenêtre doit être
située très haut dans le mur sud du Grand Palais. Très loin en
bas, vous apercevez les bâtiments de la capitale : des maisons en
miniature, regroupées à l'intérieur de la muraille blanche de la
cité. Au sud-est s'étend le lac Inrahim : une immense plaine
d'eau salée actuellement à sec et complètement craquelée. Au
nord, une route dont la chaussée surélevée conduit jusqu'à la
ville de Chula que vous distinguez à peine à l'horizon. Au sud-
ouest, vous voyez le massif montagneux du Dahir aux cimes
désolées et écrasées de soleil. Au-delà du Dahir s'étend
l'immense océan de dunes de sable, connu sous le nom de Mer de
la Sécheresse. Les barreaux de la fenêtre sont passablement
rouillés et vous devriez pouvoir les desceller sans difficulté, mais
cependant, vous vous rendez compte qu'une chute de cette
hauteur serait mortelle et vous descendez de la table. Vous
revenez rapidement sur vos pas.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome5/page_182.py", label="182", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
