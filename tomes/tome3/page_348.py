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

check_inventory(current_page_number=348, book=3)

fr_text = """
Votre Discipline Kaï vous révèle qu'il existe, à moins de 200
mètres en direction du sud, un réseau de grottes et de
souterrains. Vous abandonnez alors votre traîneau et vous partez
vers le sud pour essayer de découvrir quelque chose.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome3/page_314.py", label="314", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
