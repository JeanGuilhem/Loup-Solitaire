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

check_inventory(current_page_number=218, book=7)

fr_text = """
La première bulle explose bruyamment, et l'énorme loup noir
s'arrête brusquement en hurlant de peur. Puis il fait demi-tour et
remonte lentement le couloir en gémissant pitoyablement. Arrivé
au coin, il lance un hurlement de dépit avant de disparaître au
loin.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome7/page_151.py", label="151", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
