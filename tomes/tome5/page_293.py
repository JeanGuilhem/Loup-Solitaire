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

check_inventory(current_page_number=293, book=5)

fr_text = """
Pendant un instant, vous avez l'impression d'être en état
d'apesanteur : vous tombez et tournoyez dans le vide, totalement
inconscient des mouvements de votre corps. Vous essayez bien
de crier, mais vos cris sont emportés au loin par le vent. Soudain,
vous heurtez les plus hautes branches d'un arbre. Vous êtes
assommé par la violence du choc et votre corps se paralyse. Vous
êtes passé de vie à trépas avant même que les Drakkars ne
découvrent votre corps disloqué. Vous perdez la vie ici, et le
Sommerlund perd, lui, tout espoir de paix.
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
