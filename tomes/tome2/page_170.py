import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=170, book=2)

fr_text = """
Le garde jette un coup d'œil à votre carte de couleur blanche et renifle
avec mépris. « C'est un laissez-passer de marchand, dit-il, il ne vous
sera d'aucune utilité ici. Il vous faut un laissez-passer rouge pour avoir
accès à la base navale. » Il vous rend votre carte et retourne à son poste
de garde.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_327.py", label="327", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
