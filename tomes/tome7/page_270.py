import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=270, book=7)

fr_text = """
Vous entendez tout à coup un bruit aigu ressemblant aux
miaulements d'un millier de chats, et vous voyez de l'eau
s'échapper des yeux et de la bouche de la statue. L'écoulement
devient bientôt un véritable torrent furieux et menace d'inonder
la pièce. Vous faites demi-tour et courez vers le tunnel mais vous
découvrez avec terreur que le passage est maintenant obstrué par
un mur de pierre. L'eau vous arrive déjà à la taille, et vous
avancez en pataugeant jusqu'à la porte ovale dont vous examinez
fiévreusement la serrure.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    key = has_item("PASSE-PARTOUT")
    st.write_stream(stream_text("Si vous possédez un Passe-Partout, rendez-vous au :"))
    st.page_link("tomes/tome7/page_207.py", label="207", icon="📄", disabled=not key)

    st.write_stream(stream_text("Si vous ne possédez pas cet Objet Spécial, rendez-vous au :"))
    st.page_link("tomes/tome7/page_242.py", label="242", icon="📄", disabled=key)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
