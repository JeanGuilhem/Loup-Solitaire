import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=219, book=3)

fr_text = """
Vous sentez que le sourd grondement qui résonne dans cette
partie de la forteresse est beaucoup plus intense dans le couloir
orienté à l'ouest que dans celui orienté à l'est. Ce bruit a quelque
chose d'insolite qui vous met mal à l'aise. Vous décidez donc
d'éviter le couloir de l'ouest et d'emprunter celui de l'est.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome3/page_349.py", label="349", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
