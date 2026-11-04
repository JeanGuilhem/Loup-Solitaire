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

check_inventory(current_page_number=365, book=5)

fr_text = """
Vous sentez que l'amitié que vous offre cet homme est sincère. Si
vous acceptez son hospitalité, il pourra peut-être vous aider à
trouver Tipasa le Vagabond.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous désirez entrer dans sa maison, rendez-vous au :"))
    st.page_link("tomes/tome5/page_225.py", label="225", icon="📄")
    st.write_stream(stream_text("Si vous préférez continuer votre chemin vers Ikaresh, sans vous arrêter, rendez-vous au :"))
    st.page_link("tomes/tome5/page_272.py", label="272", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
