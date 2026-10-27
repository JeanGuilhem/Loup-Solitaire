import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=155, book=2)

fr_text = """
Vous avez parcouru un kilomètre et demi sur le chemin de gauche
lorsque vous arrivez à un long pont de pierre. Le fleuve qu'il enjambe
semble être en crue et menace de déborder de son lit. Vous vous êtes
rendu compte alors qu'il s'agit du chenal de Rynn. Il fait 3 kilomètres
dans sa plus grande largeur et près de 1500 mètres de profondeur sur
presque toute sa longueur. Il a été formé à la suite d'un glissement de
terrain qui a séparé le royaume de Durenor du reste des terres de
Magnamund. A l'entrée du pont, un poteau indicateur précise :

**PORT BAX 5 km**

Vous poussez un soupir de soulagement en constatant que vous êtes sur
le bon chemin : dans moins d'une heure, vous aurez atteint la ville.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_265.py", label="265", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
