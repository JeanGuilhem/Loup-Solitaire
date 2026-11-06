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

check_inventory(current_page_number=58, book=6)

fr_text = """
Vous sentez que vous avez profondément offensé le Kloon. Et
qu'en représailles, ce dernier est allé chercher son animal de
compagnie : un féroce chien de guerre vassagonien. Étant donné
que l'animal n'a pas été nourri depuis deux jours, il est peu
probable que vous arriviez à lui faire entendre raison ! Sans
une hésitation, vous quittez les lieux avant que le Kloon
revienne avec son molosse affamé.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_105.py", label="105", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
