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

check_inventory(current_page_number=261, book=5)

fr_text = """
Vous tombez en avant, la vue troublée par une myriade de
couleurs. Les Kraans et leurs cavaliers, le vaisseau de l'espace et
l'horizon lointain se mélangent pour former un véritable
kaléidoscope. Voici les dernières images qu'il vous est donné de
voir avant que vous ne vous écrasiez sur la terre nue et desséchée
du lac Inrahim. Votre vie se termine ici et tous les espoirs pour le
Sommerlund aussi.
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
