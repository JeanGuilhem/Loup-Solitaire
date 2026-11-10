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

check_inventory(current_page_number=195, book=7)

fr_text = """
Tout à coup, une cloche d'alarme retentit dans le couloir. Un
lourd rideau de fer tombe du plafond et ferme l'accès à la pièce.
Vous apercevez au coin, dans la pénombre, une barrière
identique qui descend devant la porte en bois par laquelle vous
êtes entré.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome7/page_37.py", label="37", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
