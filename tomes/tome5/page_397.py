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

check_inventory(current_page_number=397, book=5)

fr_text = """
Avidement, elle saisit la pièce de sa sébile, puis mord dedans
avec ses dents noircies. Rassurée sur l'authenticité de la pièce,
elle opine du chef et attend vos questions.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez lui demander si elle est bien Soushilla, rendez-vous au :"))
    st.page_link("tomes/tome5/page_307.py", label="307", icon="📄")
    st.write_stream(stream_text("Si vous préférez lui demander si elle sait où l'on peut trouver Tipasa le Vagabond, rendez-vous au :"))
    st.page_link("tomes/tome5/page_314.py", label="314", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
