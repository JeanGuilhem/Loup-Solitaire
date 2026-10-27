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

check_inventory(current_page_number=182, book=2)

fr_text = """
Il vous faut trouver un refuge pour la nuit, sinon vous risquez d'être
arrêté par les gardes de la ville. Votre Discipline Kaï vous indique
clairement qu'il vous faut retourner à la taverne pour y demander une
chambre. En y passant une bonne nuit, vous serez d'attaque demain
matin pour établir un plan qui vous permettra d'atteindre au plus vite le
royaume de Durenor.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_177.py", label="177", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
