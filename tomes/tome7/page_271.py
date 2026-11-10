import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    pickup_button,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=271, book=7)

fr_text = """
L'hideuse créature pousse un cri assourdissant tandis que vous
lui assenez le coup de grâce, puis elle s'effondre sur la plage en
soulevant dans sa chute une invraisemblable quantité de sable.
Vous apercevez une Clé d'Or, attachée à une lourde chaîne noire
autour de son estomac répugnant. Si vous souhaitez prendre
cette clé, notez-la dans la case Objets Spéciaux de votre Feuille
d'Aventure. Cette victoire vous redonne du courage, mais votre
joie est de courte durée. Vous entendez à nouveau le cri
caractéristique des rats : la chasse a repris !
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    pickup_button("CLÉ D'OR", key="cle", label="Prendre la Clé d'Or (Objet Spécial)")

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome7/page_173.py", label="173", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
