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

check_inventory(current_page_number=292, book=4)

fr_text = """
Vous dégainez votre arme juste à temps pour éviter la
catastrophe. Le disque mortel vient en effet frapper de plein
fouet le tranchant du Glaive d'Or et se brise en deux moitiés qui
vous frôlent les joues dans un sifflement terrifiant. Vous vous
éloignez ensuite du chariot en courant le long d'un sentier étroit
qui mène à une forêt dense. Lorsque vous atteignez les arbres,
vous entendez les cris des brigands derrière vous.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez courir tout droit en direction du sud, rendez-vous au :'))
    st.page_link("tomes/tome4/page_123.py", label="123", icon="📄")
    st.write_stream(stream_text("Si vous préférez changer de direction et aller vers l'ouest, rendez-vous au :"))
    st.page_link("tomes/tome4/page_169.py", label="169", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
