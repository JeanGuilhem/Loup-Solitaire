import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies, ls_death

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=253, book=3)

fr_text = """
Le Languabarb vous heurte avec tant de force que vous êtes
violemment projeté en arrière, sur la mince couche de glace qui
recouvre le lac. Assommé pour le compte, vous ne sentez même
pas que des dents pointues s'enfoncent dans votre chair. Qui
vous a dévoré ? Le Languabarb, ou la créature du lac dont vous
aviez aperçu la silhouette ? Vous ne le saurez jamais. La seule
chose certaine, c'est que votre mission s'achève ici en même
temps que votre vie.
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
