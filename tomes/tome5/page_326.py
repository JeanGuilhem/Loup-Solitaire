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

check_inventory(current_page_number=326, book=5)

fr_text = """
« Remontez la rue jusqu'au marché aux Douggas, dit alors la
vieille femme. Derrière les écuries, vous trouverez une ruelle :
Tipasa y habite la maison à la porte bleue. » Tout en prenant
garde à tenir les mains sur votre bourse de Pièces d'Or, vous vous
frayez un chemin parmi les danseurs pour gagner la porte de la
taverne, tandis que Banedon, confus et penaud, vous suit en
maugréant dans sa barbe.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome5/page_202.py", label="202", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
