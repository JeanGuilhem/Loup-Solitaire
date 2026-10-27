import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=14, book=2)

fr_text = """
Dès que la lutte s'engage, vous vous servez du pouvoir que vous donne
la Discipline Kaï pour affaiblir la concentration de votre adversaire.
Vous voyez la sueur perler à son front et ses yeux se fermer tandis qu'il
cède peu à peu sous l'effet de votre implacable Puissance Psychique.
Enfin, moins d'une minute plus tard, il s'écroule sur le sol, sans
connaissance.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_305.py", label="305", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
