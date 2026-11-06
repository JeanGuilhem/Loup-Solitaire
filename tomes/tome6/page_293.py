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

check_inventory(current_page_number=293, book=6)

fr_text = """
La porte de la tombe s'ouvre en grinçant, et aussitôt un flot de
lumière dorée inonde la crypte. L'intensité brûlante de ses rayons
paralyse instantanément le Dakomyd. Vous saisissez la Pierre de la
Sagesse et vous vous sentez animé par une force nouvelle et
empreint d'une nouvelle sagesse. Instinctivement, vous levez votre
arme et vous frappez le monstre à la base de son crâne hideux. Le
Dakomyd pousse un dernier cri puis il s'effondre au sol.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_350.py", label="350", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
